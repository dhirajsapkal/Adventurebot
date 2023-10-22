import os
import sys
from flask import Flask
from server import Config

def create_app():
    # Add the path to the server package to the Python path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the chatbot model
    from nlu.tf_model import YourTensorFlowModel
    model = YourTensorFlowModel(checkpoint_path="path/to/checkpoint")

    # Add the chatbot model to the Flask app
    app.config["chatbot_model"] = model

    return app