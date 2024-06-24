from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hrzen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Add this line to suppress the warning
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255))
    salary = db.Column(db.Float)
    email = db.Column(db.String(255), unique=True)

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
        try:
            db.session.commit()
            return jsonify({'message': 'Employee updated successfully'})
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': 'Employee with this email already exists'}), 400
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/api/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted successfully'})
    return jsonify({'message': 'Employee not found'}), 404

@app.route('/')
def home():
    return jsonify(message="Welcome to HRZen")

if __name__ == '__main__':
    app.run(debug=True)
