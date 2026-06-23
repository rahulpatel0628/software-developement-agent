from database import db
from flask_sqlalchemy import SQLAlchemy
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    def __repr__(self):
        return f"Student('{self.name}', '{self.email}')"
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    def __repr__(self):
        return f"Course('{self.name}', '{self.description}')"
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    def __repr__(self):
        return f"Enrollment('{self.student_id}', '{self.course_id}')"
class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enrollment_id = db.Column(db.Integer, db.ForeignKey('enrollment.id'), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    def __repr__(self):
        return f"Grade('{self.enrollment_id}', '{self.grade}')"