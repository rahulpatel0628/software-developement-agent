from database import db

class StudentModel:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save_to_db(self):
        new_student = db.Student(name=self.name, email=self.email, password=self.password)
        db.session.add(new_student)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return db.Student.query.filter_by(email=email).first()

class CourseModel:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def save_to_db(self):
        new_course = db.Course(name=self.name, description=self.description)
        db.session.add(new_course)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return db.Course.query.filter_by(name=name).first()

class EnrollmentModel:
    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id

    def save_to_db(self):
        new_enrollment = db.Enrollment(student_id=self.student_id, course_id=self.course_id)
        db.session.add(new_enrollment)
        db.session.commit()

    @classmethod
    def find_by_student_id_and_course_id(cls, student_id, course_id):
        return db.Enrollment.query.filter_by(student_id=student_id, course_id=course_id).first()

class GradeModel:
    def __init__(self, enrollment_id, grade):
        self.enrollment_id = enrollment_id
        self.grade = grade

    def save_to_db(self):
        new_grade = db.Grade(enrollment_id=self.enrollment_id, grade=self.grade)
        db.session.add(new_grade)
        db.session.commit()

    @classmethod
    def find_by_enrollment_id(cls, enrollment_id):
        return db.Grade.query.filter_by(enrollment_id=enrollment_id).first()
