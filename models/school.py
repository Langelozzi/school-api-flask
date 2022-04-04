#Author: Lucas Angelozzi
#Date: 28/02/22

'''This file contains the School class'''

# Imports
from models.student import Student
import json

class School:
    """This class contains information about a school and methods to manipulate the students in the school
    """
    def __init__(self, name) -> None:
        """This constructor takes the name pf the school and sets it, and opens the json file with the students and makes a list of Student objects
        representing all of the students in the school

        Args:
            name (str): The name of the school
        """
        
        self.name = name
        self.students = list()

        with open("data/school.json") as file:
            data = json.load(file)

            for object in data:
                self.students.append(Student(object["name"], object["student_id"], object["term"]))

    def __len__(self):
        """This returns the length of the students list when the length of the school object is requested

        Returns:
            int: the length of the students list
        """
        
        return len(self.students)

    def get_by_id(self, student_id):
        """This method gets a student by their id number and returns that object

        Args:
            student_id (str): the student ID of the student you want

        Returns:
            Student: the student you requested or None if the student is not found
        """
        
        for student in self.students:
            if student.student_id == student_id:
                correct_student = student
        
        try:
            return correct_student
        except:
            return None #if you dont do a return statement at all then it also returns None

    def get_by_name(self, name):
        """This method gets all students with the specific name and returns those objects

        Args:
            name (str): the name of the students you want

        Returns:
            list: the students you requested (empty if no students with that name)
        """
        
        matches = list()

        # doing the same thing using list comprehension
        '''matches = [
            student
            for student in self.students
            if student.name == name
        ]'''

        for student in self.students:
            if student.name == name:
                matches.append(student)
        
        return matches

    def add(self, instance: Student):
        """This method takes a student instance and adds it to the list of the students in the school

        Args:
            instance (Student): the student you want to add
        """
        
        self.students.append(instance)
    
    def delete(self, student_id):
        """This method deletes a student by their ID number

        Args:
            student_id (str): the student ID of the student you want to delete

        Returns:
            bool: True if the student was successfully deleted
        """
        
        ret = False

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                ret = True
        
        return ret

    def save(self):
        """This method writes the changes you made to the school to the JSON file
        """
        
        # Using list comprehension to create list
        '''
        data = [
            student.to_dict()
            for student in self.students
        ]
        '''

        json_data = list()
        for student in self.students:
            json_data.append(student.to_dict())

        with open("data/school.json", "w") as file:
            json.dump(json_data, file)


