from typing import Optional
from pydantic import BaseModel, Field, EmailStr

# Define the Student model, inheriting from Pydantic's BaseModel
class Student(BaseModel):
    # Required string field with a default value
    name: str = 'Bilal Shabbir'
    
    # Optional integer field (can be an int or None)
    age: Optional[int] = None
    
    # Required field validated as a standard email string
    email: EmailStr
    
    # Required float field with validation and a description
    # gt=0: value must be greater than 0
    # lt=10: value must be less than 10
    # default=5: default value if not provided
    cgpa: float = Field(
        gt=0, 
        lt=10, 
        default=5, 
        description='A decimal value representing the cgpa of the student'
    )

# Input data to create a new student instance
# Note: 'name' is omitted, so it will use the default 'nitish'
# Note: 'cgpa' is omitted, so it will use the default 5
new_student = {'age': '32', 'email': 'abc@gmail.com'}

# Instantiate the Student model using dictionary unpacking (**)
# Pydantic will validate the data and perform type coercion (e.g., '32' to 32)
student = Student(**new_student)

# Print the resulting Student object (Pydantic models implement __repr__)
print(type(student))
print(student)
student_dict = dict(student)
print(student_dict)
print(student_dict['age'])
student_json = student.model_dump_json()
print(student_json)