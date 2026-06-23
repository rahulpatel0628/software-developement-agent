from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from models import StudentModel, CourseModel, EnrollmentModel, GradeModel
from database import db

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if not name or not email or not password:
        return jsonify({'message': 'Name, email, and password are required'}), 400
    student = StudentModel(name, email, password)
    student.save_to_db()
    return jsonify({'message': 'Student created successfully'}), 201

@main_routes.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    name = data.get('name')
    description = data.get('description')
    if not name or not description:
        return jsonify({'message': 'Name and description are required'}), 400
    course = CourseModel(name, description)
    course.save_to_db()
    return jsonify({'message': 'Course created successfully'}), 201

@main_routes.route('/enrollments', methods=['POST'])
def create_enrollment():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    if not student_id or not course_id:
        return jsonify({'message': 'Student ID and course ID are required'}), 400
    enrollment = EnrollmentModel(student_id, course_id)
    enrollment.save_to_db()
    return jsonify({'message': 'Enrollment created successfully'}), 201

@main_routes.route('/grades', methods=['POST'])
def create_grade():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    enrollment_id = data.get('enrollment_id')
    grade = data.get('grade')
    if not enrollment_id or not grade:
        return jsonify({'message': 'Enrollment ID and grade are required'}), 400
    grade_model = GradeModel(enrollment_id, grade)
    grade_model.save_to_db()
    return jsonify({'message': 'Grade created successfully'}), 201

@main_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No data provided'}), 400
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400
    student = StudentModel.find_by_email(email)
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    if not student.check_password(password):
        return jsonify({'message': 'Invalid password'}), 401
    access_token = create_access_token(identity=student.id)
    return jsonify({'access_token': access_token}), 200

@main_routes.route('/students/<int:student_id>', methods=['GET'])
@jwt_required
def get_student(student_id):
    student = StudentModel.find_by_id(student_id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404
    return jsonify({'name': student.name, 'email': student.email}), 200

@main_routes.route('/courses/<int:course_id>', methods=['GET'])
@jwt_required
def get_course(course_id):
    course = CourseModel.find_by_id(course_id)
    if not course:
        return jsonify({'message': 'Course not found'}), 404
    return jsonify({'name': course.name, 'description': course.description}), 200

@main_routes.route('/enrollments/<int:enrollment_id>', methods=['GET'])
@jwt_required
def get_enrollment(enrollment_id):
    enrollment = EnrollmentModel.find_by_id(enrollment_id)
    if not enrollment:
        return jsonify({'message': 'Enrollment not found'}), 404
    return jsonify({'student_id': enrollment.student_id, 'course_id': enrollment.course_id}), 200

@main_routes.route('/grades/<int:grade_id>', methods=['GET'])
@jwt_required
def get_grade(grade_id):
    grade = GradeModel.find_by_id(grade_id)
    if not grade:
        return jsonify({'message': 'Grade not found'}), 404
    return jsonify({'enrollment_id': grade.enrollment_id, 'grade': grade.grade}), 200
