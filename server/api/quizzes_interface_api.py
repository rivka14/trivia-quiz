from flask import Flask, request, jsonify, Blueprint
from business_logic.auth import decode_token
from business_logic.admin_interface import (
    create_new_quiz,
    edit_quiz,
    activate_quiz,
    get_quiz_statistics,
    view_quizzes,
)
import dotenv

from api.auth_api import token_required

quizzes_interface_api = Blueprint('admin_api', __name__)

# Load environment variables
dotenv.load_dotenv()


@quizzes_interface_api.route('/admin/create_quiz', methods=['POST'])
@token_required
def api_create_quiz(user_id):
    data = request.get_json()
    name = data.get('name')
    questions = data.get('questions')
    
    if not name or not questions:
        return jsonify({'error': 'Missing required fields.'}), 400
    
    response, status = create_new_quiz(name=name, user_id=user_id, questions=questions)
    return jsonify(response), status

@quizzes_interface_api.route('/admin/edit_quiz/<quiz_id>', methods=['PUT'])
@token_required
def api_edit_quiz(user_id, quiz_id):
    data = request.get_json()
    name = data.get('name')
    questions = data.get('questions')
    correct_options = data.get('correct_options')
    
    response, status = edit_quiz(quiz_id=quiz_id, user_id=user_id, name=name, questions=questions, correct_options=correct_options)
    return jsonify(response), status

@quizzes_interface_api.route('/admin/activate_quiz/<quiz_id>', methods=['POST'])
@token_required
def api_activate_quiz(user_id, quiz_id):
    response, status = activate_quiz(quiz_id=quiz_id, user_id=user_id)
    return jsonify(response), status

@quizzes_interface_api.route('/admin/view_quizzes', methods=['GET'])
@token_required
def api_view_quizzes(user_id):
    response, status = view_quizzes(user_id)
    return jsonify(response), status

@quizzes_interface_api.route('/admin/quiz_statistics/<quiz_id>', methods=['GET'])
@token_required
def api_quiz_statistics(user_id, quiz_id):
    response, status = get_quiz_statistics(quiz_id=quiz_id, user_id=user_id)
    return jsonify(response), status

