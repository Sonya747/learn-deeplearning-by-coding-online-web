from typing import List
from sqlmodel import Field, SQLModel, Relationship

class User(SQLModel,table=True):
    id: int = Field(primary_key=True,index=True) #学号
    username: str = Field(default=None)
    password: str = Field(default=None)

class Teacher(SQLModel,table=True):
    id: int = Field(primary_key=True, index=True)
    name: str = Field(default=None)
    classes: List["Class"]|None = Relationship(back_populates="teacher")

class Quiz(SQLModel,table = True):
    id: int = Field(primary_key=True, index=True)
    content: str = Field(default=None)
    answer: str = Field(default=None)
    output: str = Field(default=None)

class Class(SQLModel,table = True):
    id: int = Field(primary_key=True, index=True)
    name: str = Field(default=None)
    teacher_id: int = Field(foreign_key="teacher.id")
    teacher: Teacher = Relationship(back_populates="classes")
    students: List["Student"]|None = Relationship(back_populates="class_")

class Student(SQLModel,table =True):
    id: int = Field(primary_key=True, index=True)
    name: str = Field(default=None)
    grade: int = Field(default=0)
    class_id: int = Field(foreign_key='class.id')
    class_: Class|None = Relationship(back_populates="students")

class Record(SQLModel,table =True):
    id:int|None = Field(default=None,primary_key=True)
    student_id: int = Field(foreign_key='student.id')
    quiz_id: int = Field(foreign_key='quiz.id')
    result: str = Field(default="Fail")
