from flask import Blueprint, jsonify, request
from models import Student, Course, Enrollment, Grade
from database import db
main_routes = Blueprint('main_routes', __name__)
@main_routes.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    output = []
    for student in students:
        student_data = {'id': student.id, 'name': student.name, 'email': student.email}
        output.append(student_data)
    return jsonify({'students': output})
@main_routes.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    output = []
    for course in courses:
        course_data = {'id': course.id, 'name': course.name, 'description': course.description}
        output.append(course_data)
    return jsonify({'courses': output})
@main_routes.route('/enrollments', methods=['GET'])
def get_enrollments():
    enrollments = Enrollment.query.all()
    output = []
    for enrollment in enrollments:
        enrollment_data = {'id': enrollment.id, 'student_id': enrollment.student_id, 'course_id': enrollment.course_id}
        output.append(enrollment_data)
    return jsonify({'enrollments': output})
@main_routes.route('/grades', methods=['GET'])
def get_grades():
    grades = Grade.query.all()
    output = []
    for grade in grades:
        grade_data = {'id': grade.id, 'enrollment_id': grade.enrollment_id, 'grade': grade.grade}
        output.append(grade_data)
    return jsonify({'grades': output})