from flask import Blueprint, request, jsonify
from nlu.nlp_model import process_user_input

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    memory = {}  # Retrieve memory from memory_manager or a database
    response, memory_update = process_user_input(user_input, memory)
    # Update memory with memory_update
    return jsonify({'response': response})
