# HRZen Backend

HRZen is a simple employee management REST API built with Flask and SQLAlchemy.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)

### Installation

1. Clone the repository:
   
   git clone https://github.com/KenzaDahhoum/portfolio-project.git
   cd portfolio-project/hrzen_backend

2. Install the required packages:
   pip3 install -r requirements.txt
   pip3 install Flask==1.1.2 Flask-SQLAlchemy==2.5.1

3. Set up the database:
    python3
    >>> from app import db
    >>> db.create_all()
    >>> exit()

4. Running the Application
    flask run
5. API Endpoints:
    Get All Employees
         URL: /api/employees
    Add a New Employee
         URL: /api/employees
    Update an Employee
        URL: /api/employees/<id>
    Delete an Employee
        URL: /api/employees/<id>

Yes, you should include the instruction to install the required packages in your README.md file. Here is the complete README.md file with that section properly included:

markdown
Copy code
# HRZen Backend

HRZen is a simple employee management REST API built with Flask and SQLAlchemy.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or later
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>/hrzen_backend
Install the required packages:

bash
Copy code
pip3 install Flask==1.1.2 Flask-SQLAlchemy==2.5.1
Set up the database:

bash
Copy code
python3
>>> from app import db
>>> db.create_all()
>>> exit()
Running the Application
To start the Flask development server, run the following command:

bash
Copy code
flask run
The application will be accessible at http://127.0.0.1:5000/.

API Endpoints
Get All Employees
URL: /api/employees
Method: GET
Response:
json
Copy code
[
  {
    "id": 1,
    "name": "John Doe",
    "position": "Developer",
    "salary": 60000,
    "email": "john.doe@example.com"
  }
]
Add a New Employee
URL: /api/employees
Method: POST
Request Body:
json
Copy code
{
  "name": "John Doe",
  "position": "Developer",
  "salary": 60000,
  "email": "john.doe@example.com"
}
Response:
json
Copy code
{
  "message": "Employee added successfully"
}
Update an Employee
URL: /api/employees/<id>
Method: PUT
Request Body:
json
Copy code
{
  "name": "John Doe Updated",
  "position": "Lead Developer",
  "salary": 70000,
  "email": "john.doe@example.com"
}
Response:
json
Copy code
{
  "message": "Employee updated successfully"
}
Delete an Employee
URL: /api/employees/<id>
Method: DELETE
Response:
json
Copy code
{
  "message": "Employee deleted successfully"
}
5. Error Handling
The API returns appropriate error messages and status codes for various error conditions, such as missing fields in the request or unique constraint violations.
6. Built With
Flask - A micro web framework for Python
SQLAlchemy - The Python SQL toolkit and Object Relational Mapper
7. Author
KENZA DAHHOUM - FullStack Developer - KenzaDahhoum
8. Acknowledgments
Flask documentation
SQLAlchemy documentation