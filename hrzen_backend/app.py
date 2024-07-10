import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from functools import wraps

app = Flask(__name__)
CORS(app, origins=["http://localhost:8080", "https://hrzen-lfsf.onrender.com"])

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

db = SQLAlchemy(app)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            token = token.split()[1]  
            print(f"Token received: {token}")
            data = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
            print(f"Decoded token data: {data}")
            current_user = Employee.query.filter_by(id=data['id']).first()
            if not current_user:
                return jsonify({'message': 'User not found!'}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError as e:
            print(f"Token error: {e}")
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255))
    salary = db.Column(db.Float)
    email = db.Column(db.String(255), unique=True)
    role = db.Column(db.String(50), nullable=False, default='employee')
    password = db.Column(db.String(255), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    employee = db.relationship('Employee', backref=db.backref('attendance', lazy=True))

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = Employee(
        name=data['name'],
        position=data.get('position', ''),
        salary=data.get('salary', 0.0),
        email=data['email'],
        role=data['role'],
        password=hashed_password
    )
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Registered successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'User with this email already exists'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'message': 'Email and password are required'}), 400

    user = Employee.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode({'id': user.id, 'exp': datetime.utcnow() + timedelta(hours=24)}, app.config['JWT_SECRET_KEY'], algorithm=["HS256"])
        print(f"Token generated: {token}")
        return jsonify({'token': str(token), 'role': user.role}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.json
    try:
        user_id = jwt.decode(data['token'].split()[1], app.config['JWT_SECRET_KEY'], algorithms=["HS256"])['id']
        user = Employee.query.get(user_id)
        if user and check_password_hash(user.password, data['current_password']):
            user.password = generate_password_hash(data['new_password'], method='sha256')
            db.session.commit()
            return jsonify({'message': 'Password changed successfully'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired!'}), 403
    except jwt.InvalidTokenError as e:
        print(f"Token error: {e}")
        return jsonify({'message': 'Token is invalid!'}), 403

@app.route('/api/employees', methods=['GET'])
@token_required
def get_employees(current_user):
    if current_user.role != 'manager':
        return jsonify({'message': 'Permission denied!'}), 403
    employees = Employee.query.filter(Employee.role != 'manager').all()
    return jsonify([{
        'id': emp.id, 'name': emp.name, 'position': emp.position, 'salary': emp.salary, 'email': emp.email, 'role': emp.role
    } for emp in employees])

@app.route('/api/employees', methods=['POST'])
@token_required
def add_employee(current_user):
    if current_user.role != 'manager':
        return jsonify({'message': 'Permission denied!'}), 403
    data = request.json
    required_fields = ['name', 'email', 'role', 'password']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'{field} is required'}), 400

    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_employee = Employee(
        name=data['name'],
        position=data.get('position', ''),
        salary=data.get('salary', 0),
        email=data['email'],
        role=data['role'],
        password=hashed_password
    )
    try:
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Employee added successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Employee with this email already exists'}), 400

@app.route('/api/employees/<int:id>', methods=['PUT'])
@token_required
def update_employee(current_user, id):
    if current_user.role != 'manager':
        return jsonify({'message': 'Permission denied!'}), 403
    data = request.json
    employee = Employee.query.get(id)
    if employee:
        employee.name = data['name']
        employee.position = data['position']
        employee.salary = data['salary']
        employee.email = data['email']
        employee.role = data['role']
        if 'password' in data:
            employee.password = generate_password_hash(data['password'], method='sha256')
        db.session.commit()
        return jsonify({'message': 'Employee updated successfully'})
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/api/employees/<int:id>', methods=['DELETE'])
@token_required
def delete_employee(current_user, id):
    if current_user.role != 'manager':
        return jsonify({'message': 'Permission denied!'}), 403
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted successfully'})
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/api/events', methods=['GET'])
@token_required
def get_events(current_user):
    events = Event.query.all()
    return jsonify([{
        'id': event.id, 'title': event.title, 'date': event.date.strftime('%Y-%m-%d')
    } for event in events])

@app.route('/api/events', methods=['POST'])
@token_required
def add_event(current_user):
    data = request.json
    try:
        date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
    except ValueError:
        return jsonify({'message': 'Invalid date format'}), 400
    new_event = Event(title=data['title'], date=date)
    db.session.add(new_event)
    db.session.commit()
    return jsonify({'message': 'Event added successfully'}), 201

@app.route('/api/events/<int:id>', methods=['PUT'])
@token_required
def update_event(current_user, id):
    data = request.json
    event = Event.query.get(id)
    if event:
        try:
            event.date = datetime.strptime(data['date'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
        except ValueError:
            return jsonify({'message': 'Invalid date format'}), 400
        event.title = data['title']
        db.session.commit()
        return jsonify({'message': 'Event updated successfully'})
    return jsonify({'message': 'Event not found'}), 404

@app.route('/api/events/<int:id>', methods=['DELETE'])
@token_required
def delete_event(current_user, id):
    event = Event.query.get(id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted successfully'})
    return jsonify({'message': 'Event not found'}), 404

@app.route('/api/attendance', methods=['GET'])
@token_required
def get_attendance(current_user):
    attendance_records = Attendance.query.join(Employee).all()
    return jsonify([{
        'id': record.id,
        'employee_id': record.employee_id,
        'employee_name': record.employee.name,
        'date': record.date.strftime('%Y-%m-%d'),
        'status': record.status
    } for record in attendance_records])

@app.route('/api/attendance', methods=['POST'])
@token_required
def add_attendance(current_user):
    data = request.json
    new_attendance = Attendance(employee_id=data['employee_id'], date=datetime.strptime(data['date'], '%Y-%m-%d').date(), status=data['status'])
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify({'message': 'Attendance added successfully'}), 201

@app.route('/api/attendance/<int:id>', methods=['PUT'])
@token_required
def update_attendance(current_user, id):
    data = request.json
    attendance = Attendance.query.get(id)
    if attendance:
        attendance.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        attendance.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Attendance updated successfully'})
    return jsonify({'message': 'Attendance not found'}), 404

@app.route('/api/attendance/<int:id>', methods=['DELETE'])
@token_required
def delete_attendance(current_user, id):
    attendance = Attendance.query.get(id)
    if attendance:
        db.session.delete(attendance)
        db.session.commit()
        return jsonify({'message': 'Attendance deleted successfully'})
    return jsonify({'message': 'Attendance not found'}), 404

@app.route('/')
def home():
    return jsonify(message="Welcome to HRZen")

if __name__ == '__main__':
    if os.environ.get('INIT_DB') == 'True':
        with app.app_context():
            db.create_all()
            print("Initialized the database schema")
    app.run(debug=True)
