from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hrzen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255))
    salary = db.Column(db.Float)
    email = db.Column(db.String(255), unique=True)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), nullable=False)

db.create_all()

@app.route('/api/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        'id': emp.id, 'name': emp.name, 'position': emp.position, 'salary': emp.salary, 'email': emp.email
    } for emp in employees])

@app.route('/api/employees', methods=['POST'])
def add_employee():
    data = request.json
    if 'name' not in data or 'email' not in data:
        return jsonify({'message': 'Name and Email are required'}), 400

    new_employee = Employee(name=data['name'], position=data['position'], salary=data['salary'], email=data['email'])
    try:
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Employee added successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Employee with this email already exists'}), 400

@app.route('/api/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    employee = Employee.query.get(id)
    if employee:
        employee.name = data['name']
        employee.position = data['position']
        employee.salary = data['salary']
        employee.email = data['email']
        db.session.commit()
        return jsonify({'message': 'Employee updated successfully'})
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/api/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted successfully'})
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/api/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{
        'id': event.id, 'title': event.title, 'date': event.date.strftime('%Y-%m-%d')
    } for event in events])

@app.route('/api/events', methods=['POST'])
def add_event():
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
def update_event(id):
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
def delete_event(id):
    event = Event.query.get(id)
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({'message': 'Event deleted successfully'})
    return jsonify({'message': 'Event not found'}), 404

@app.route('/api/attendance', methods=['GET'])
def get_attendance():
    attendance = Attendance.query.all()
    return jsonify([{
        'id': att.id, 'employee_id': att.employee_id, 'date': att.date.strftime('%Y-%m-%d'), 'status': att.status
    } for att in attendance])

@app.route('/api/attendance', methods=['POST'])
def add_attendance():
    data = request.json
    new_attendance = Attendance(employee_id=data['employee_id'], date=datetime.strptime(data['date'], '%Y-%m-%d').date(), status=data['status'])
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify({'message': 'Attendance added successfully'}), 201

@app.route('/api/attendance/<int:id>', methods=['PUT'])
def update_attendance(id):
    data = request.json
    attendance = Attendance.query.get(id)
    if attendance:
        attendance.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        attendance.status = data['status']
        db.session.commit()
        return jsonify({'message': 'Attendance updated successfully'})
    return jsonify({'message': 'Attendance not found'}), 404

@app.route('/api/attendance/<int:id>', methods=['DELETE'])
def delete_attendance(id):
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
    app.run(debug=True)