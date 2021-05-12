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
from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

DeclBase = declarative_base()

engine = sqlalchemy.create_engine('sqlite:///students.sqlite3', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Program(DeclBase):
    __tablename__ = 'programs'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", backref="program")
    program_courses = relationship("Course", backref="program")

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
    
    programs_courses = relationship("Programs_course", backref="course")
    scores = relationship("Score", backref="course")
    
    def __init__(self, name):
        self.name = name 
        
class Programs_course(DeclBase):
    __tablename__ = 'programs_courses'
    __table_args__ = {'extend_existing': True}
    __table_args__ = (PrimaryKeyConstraint('semester_number', 'course_id', 'program_id'),)
   
    semester_number = Column(Integer)
    course_id = Column(Integer, ForeignKey('courses.id'))
    program_id = Column(Integer, ForeignKey('programs.id'))
    
    def __init__(self, semester_number, course, program):
        self.semester_number = semester_number
        self.course = course
        self.program = program
        
class Score(DeclBase):
    __tablename__ = 'scores'
    __table_args__ = {'extend_existing': True}
    __table_args__ = (PrimaryKeyConstraint('student_id', 'course_id'),)
    score = Column(Integer)
    
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    
    def __init__(self, score, student, course):
        self.score = score
        self.student = student
        self.course = course
        
        
se1 = Program("Стоматология")
se2 = Program("Лечебное дело")

st1 = Student("00001", "Иванов", "Артём", "Михайлович", se1)
st2 = Student("00002", "Простакова", "Виолетта", "Игоревна", se1)
st3 = Student("00003", "Крюков", "Николай", "Николаевич", se2)
st4 = Student("00004", "Лебедева", "Дарья", "Алексеевна", se2)

session.add_all([st1, st2, st3, st4])
session.commit()

co1 = Course("Биофизика")
se3 = Program("Биоинформатика")

pc1 = Programs_course("2", co1, se3)

session.add(pc1)
try:
    session.commit()
except:
    raise
finally:
    session.close()
    
import sys

print("Программы и студенты")
for p in session.query(Program):
    print("Программа: ", p.name)
    for s in p.students:
        print("- ", s.name, s.surname, s.patronymic, s.card)
    for pc in p.program_courses:
        print("   - ", pc.program.name, pc.course.name, pc.semester_number)
session.commit()

print("Курсы: ")
for p in session.query(Course):
    print("Курс: ", p.name)
    
pr = session.query(Program).filter_by(name="Биоинформатика")[0]
st = session.query(Student).filter_by(name="Виолетта")[0]

st.program = pr
session.commit()

print("Программы и студенты")
for p in session.query(Program):
    print("Программа: ", p.name)
    for s in p.students:
        print("- ", s.name)
session.commit()

co2 = Course("Педиатрия")

pc2 = Programs_course("4", co2, se2)

session.add(pc2)
try:
    session.commit()
except:
    raise
    
print("Программы и студенты")
for p in session.query(Program):
    print("Программа: ", p.name)
    for s in p.students:
        print("- ", s.name, s.surname, s.patronymic, s.card)
    for pc in p.program_courses:
        print("   - ", pc.program.name, pc.course.name, pc.semester_number)
session.commit()


print("Курсы")
for p in session.query(Course):
    print("Курс: ", p.name, p.id)
    
sc1 = Score("4", st3, co2)

session.add(sc1)
try:
    session.commit()
except:
    raise
finally:
    session.close()
    
print("Студенты и оценки: ")
for p in session.query(Student):
    print("Студент: ", p.name)
    for pc in p.scores:
        print("- ", pc.student.name, pc.course.name, pc.score)
session.commit()
