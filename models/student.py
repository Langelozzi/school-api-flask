#Author: Lucas Angelozzi
#Date: 28/02/22

'''This file contains the Student class'''

class Student:
    """This class contians basic information about a student at BCIT
    """
    def __init__(self, name: str, student_id: str, term = 1) -> None:
        """This constructor will initialize the name, id number and term for each student, raising 
        error when the given items are not valid

        Args:
            name (str): The students name
            student_id (str): The students BCIT ID number
            term (int, optional): The term number the student is currently in. Defaults to 1.

        Raises:
            ValueError: if the name is empty or not a string  
            ValueError: if the student_id isnt a string following the format "A0xxxxxxx"
            ValueError: if the term is not a valid integer
        """
        
        if (name == None) or (type(name) != str):
            raise ValueError
        if (type(student_id) != str) or (len(student_id) != 9) or (student_id[0] != 'A') or (student_id[1] != '0'):
            raise ValueError
        if (type(term) != int):
            raise ValueError
        
        self.name = name
        self.student_id = student_id
        self.term = term

    def to_dict(self) -> dict:
        """This method returns a dictionary containing the students information

        Returns:
            dict: the students information
        """

        return {"name": self.name, "student_id": self.student_id, "term": self.term}