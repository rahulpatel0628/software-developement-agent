from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from database import session
from models import Student, Course, Enrollment, Grade

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/students', methods=['GET'])
@jwt_required
def get_students():
    students = session.query(Student).all()
    return jsonify([{'id': s.id, 'name': s.name, 'email': s.email} for s in students])

@main_routes.route('/courses', methods=['GET'])
@jwt_required
def get_courses():
    courses = session.query(Course).all()
    return jsonify([{'id': c.id, 'name': c.name, 'description': c.description} for c in courses])

@main_routes.route('/enrollments', methods=['GET'])
@jwt_required
def get_enrollments():
    enrollments = session.query(Enrollment).all()
    return jsonify([{'id': e.id, 'student_id': e.student_id, 'course_id': e.course_id} for e in enrollments])

@main_routes.route('/grades', methods=['GET'])
@jwt_required
def get_grades():
    grades = session.query(Grade).all()
    return jsonify([{'id': g.id, 'enrollment_id': g.enrollment_id, 'grade': g.grade} for g in grades])
