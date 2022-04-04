#Author: Lucas Angelozzi
#Date: 28/02/22

'''This file contains API endpoints to perform different modifications on the school'''

# Imports
from flask import Flask, jsonify, request, render_template
from models.school import School
from models.student import Student

# Creates an instance of a flask application
app = Flask(__name__)

# Homepage with table of students
@app.route("/")
def show_table():
    """This function will return an html page with a table of all the students in the school

    Returns:
        HTML Template: The HTML page with the table
    """
    bcit = School("BCIT")

    return render_template("home.html", school=bcit)

# Get all the students in the school
@app.route("/students", methods=["GET"])
def get_students():
    """This function returns JSON objects for every student in the school

    Returns:
        JSON: Objects representing all of the students
    """

    bcit = School("BCIT")

    # Same as below but using list comprehension
    '''
    data = [
        student.to_dict()
        for student in bcit.students
    ]
    '''

    as_dicts = list()
    for student in bcit.students:
        as_dicts.append(student.to_dict())

    return jsonify(as_dicts), 200

# Get a single student by student id
@app.route("/student/<string:student_id>", methods=["GET"])
def get_one_student(student_id = None):
    """This function returns a single student as a JSON object

    Args:
        student_id (str): The student ID of the student you want to get. Defaults to None.

    Returns:
        JSON: The JSON object of the student you want.
    """
    
    bcit = School("BCIT")

    if student_id == None:
        return "No student ID provided as argument", 400
    
    student = bcit.get_by_id(student_id)
    
    if student == None:
        return "No such student", 404
    else:
        return jsonify(student.to_dict())

# POST method to add a student to the school
@app.route("/student", methods=["POST"])
def add_student():
    """This function used the POST method to add a new student to the school

    Returns:
        str: A string with status information and a status code.
    """
    
    bcit = School("BCIT")
    data = request.json

    try:
        # Using dictionary unpacking to create the new student because keys are same name as attributes
        '''new_student = Student(**data)'''
        new_student = Student(data["name"], data["student_id"], data["term"])
    except ValueError:
        return "Invalid data entries", 400

    bcit.add(new_student)
    bcit.save()

    return "", 201

# PUT method to update a student by ID
@app.route("/student/<string:student_id>", methods=["PUT"])
def update_student(student_id):
    """This function finds a student by ID and updates their information

    Args:
        student_id (str): The student ID of the student you want to update

    Returns:
        str: a string containing status information and a status code
    """
    
    bcit = School("BCIT")
    data = request.json

    correct_student = bcit.get_by_id(student_id)
    if correct_student == None:
        return "No student found", 404

    for attribute in ("name", "student_id", "term"):
        if attribute in data:
            #sets the "attribute" attribute for correct student and sets it to the value data[attribute]
            setattr(correct_student, attribute, data[attribute])

    bcit.save()

    return "", 201
    
# DELETE method to delete a student by ID
@app.route("/student/<string:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """This function deletes the student whos ID is specified

    Args:
        student_id (str): The Student ID of the student you want to delete

    Returns:
        str: a string containing status information and a status code
    """
    
    bcit = School("BCIT")

    status = bcit.delete(student_id)

    bcit.save()

    if status == True:
        return "", 201
    elif status == False:
        return "Student not found", 404
    

if __name__ == "__main__":
    #debug=True means it will refresh after each change the same way nodemon does
    app.run(debug=True)