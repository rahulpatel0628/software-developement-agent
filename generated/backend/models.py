from database import Base, session
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(200))

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    student = relationship('Student', backref='enrollments')
    course = relationship('Course', backref='enrollments')

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    enrollment_id = Column(Integer, ForeignKey('enrollments.id'))
    grade = Column(Float)
    enrollment = relationship('Enrollment', backref='grades')
