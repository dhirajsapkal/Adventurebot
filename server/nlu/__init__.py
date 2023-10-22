import os
import sys
from flask import Flask
from server.config import Config
from server.chatbot import YourTensorFlowModel
import openai

def create_app():
    # Add the path to the server package to the Python path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the chatbot model
    model = YourTensorFlowModel(checkpoint_path="path/to/checkpoint")

    # Initialize the ChatGPT model
    openai.api_key = "YOUR_API_KEY"
    chatgpt_model = openai.Completion.create(
        engine="davinci",
        prompt="",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Add the chatbot and ChatGPT models to the Flask app
    app.config["chatbot_model"] = model
    app.config["chatgpt_model"] = chatgpt_model

    # Define the active selection method
    def active_selection(model, prompt, responses):
        scores = []
        for response in responses:
            input_text = prompt + response
            score = model.score(input_text)
            scores.append(score)
        max_score_index = scores.index(max(scores))
        return responses[max_score_index]

    # Add the active selection method to the Flask app
    app.config["active_selection"] = active_selection

    return app