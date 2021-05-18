# -*- coding: utf-8 -*-
"""
Created on Tue May 18 18:29:51 2021

@author: Карина
"""

import sqlite3 as dbms

conn = dbms.connect("students.sqlite3")
cursor = conn.cursor()

with open("11.drop_ddl.sql", 'r', encoding='utf-8') as f:
    drop_ddl = f.read()
with open("11.create_ddl.sql", 'r', encoding='utf-8') as f:
    create_ddl = f.read()
    
if True:
    cursor.executescript(drop_ddl)
    conn.commit()
if True:
    cursor.executescript(create_ddl)
    conn.commit()
    
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

DeclBase = declarative_base()

engine = sqlalchemy.create_engine('sqlite:///students.sqlite3', echo=False)  # echo=True для логгинга
Session = sessionmaker(bind=engine)
session = Session()

null=True
class Program(DeclBase):
    __tablename__ = 'programs'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", backref="program")
    programs_courses = relationship("Program_course", backref="program")

    def __init__(self, name):
        self.name = name

class Student(DeclBase):
    __tablename__ = 'students'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    card = Column(String)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    
    program_id = Column(Integer, ForeignKey('programs.id'))
    marks = relationship("Mark", backref="student")
    
    def __init__(self, card, surname, name, patronymic, program):
        self.card = card
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.program = program
        
class Course(DeclBase):
    __tablename__ = 'courses'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    programs_courses = relationship("Program_course", backref="course")
    marks = relationship("Mark", backref="course")
    
    def __init__(self, name):
        self.name = name
        
class Program_course(DeclBase):
    __tablename__ = 'programs_courses'
    __table_args__ = {'extend_existing': True}
    semester_number = Column(Integer, primary_key=True)
    
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    program_id = Column(Integer, ForeignKey('programs.id'), primary_key=True)
    
    def __init__(self, semester_number, course, program):
        self.semester_number = semester_number
        self.course = course
        self.program = program
        
class Mark(DeclBase):
    __tablename__ = 'marks'
    __table_args__ = {'extend_existing': True}
    mark = Column(Integer)
    
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    
    def __init__(self, mark, student, course):
        self.mark = mark
        self.student = student
        self.course = course
        
se1 = Program("Програмная инженерия")
se2 = Program("Теоретическая физика")

st1 = Student("002001", "Иванов", "Артём", "Михайлович", se1)
st2 = Student("002002", "Простакова", "Виолетта", "Игоревна", se1)
st3 = Student("002003", "Крюков", "Николай", "Николаевич", se2)
st4 = Student("002004", "Лебедева", "Дарья", "Алексеевна", se2)

c1 = Course("Алгебра")

pc1 = Program_course("4", c1, se1)
pc2 = Program_course("2", c1, se2)

m1 = Mark("5", st1, c1)
m2 = Mark("4", st2, c1)
m3 = Mark("3", st3, c1)
m4 = Mark("5", st4, c1)

session.add_all([st1, st2, st3, st4, c1, pc1, pc2, m1, m2, m3, m4])
session.commit()

import sys

print("Программы и студенты:")
for p in session.query(Program):
    print("Программа: ", p.name)
    for s in p.students:
        print("- ", s.name, s.surname)
    for pc in p.programs_courses:
        print("Номер семестра", pc.semester_number)
        
for pc in p.programs_courses:
        print("   - ", pc.program.name, pc.course.name, pc.semester_number)
        
print("Cтуденты и оценки: ")
for p in session.query(Student):
    print("Студент: ", p.name)
    for pc in p.marks:
        print("- ", pc.student.name, pc.student.surname, pc.course.name, pc.mark)

session.commit()