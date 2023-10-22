# AdventureBot Project Overview

AdventureBot is a self-improving AI chatbot project aimed at building a TensorFlow-based model that continuously learns and improves over time with an ability to retain memory across interactions. It integrates ChatGPT for enhanced NLP capabilities, especially in the early stages of the project.

## Directory Structure

```plaintext
my_project/
├─ server/
│  ├─ api/
│  │  ├─ __init__.py
│  │  └─ routes.py
│  ├─ config/
│  │  └─ config.py
│  ├─ nlu/
│  │  └─ nlp_model.py
│  ├─ memory/
│  │  └─ memory_manager.py
│  ├─ tests/
│  ├─ logs/
│  ├─ __init__.py
│  ├─ app.py
│  └─ requirements.txt
├─ frontend1/
│  ├─ index.html
│  ├─ style.css
│  └─ script.js
├─ README.md
└─ LICENSE

```
The server directory contains the Flask app and its components, including the API, configuration, NLP model, memory manager, and automated training script. The frontend1 directory contains the frontend code for the chatbot interface. The README.md file provides an overview of the project, and the LICENSE file contains the project's license.

## Installation and usage

### Prerequisites
Before you begin, make sure you have the following installed:

- Python 3.6 or higher
- Flask
- TensorFlow
- OpenAI API key

### Installation
- Clone the AdventureBot repository to your local machine: ```git clone https://github.com/your_username/AdventureBot.git```
- Navigate to the server directory: ```cd AdventureBot/server```
- Install the required Python packages: ```pip install -r requirements.txt```
- Set up your OpenAI API key by creating a .env file in the server directory and adding the following line: ```OPENAI_API_KEY=your_api_key_here```
- Start the Flask app: ```python app.py```
    - Open your web browser and navigate to http://localhost:5000 to access the chatbot interface.

### Project Structure
The AdventureBot project consists of the following components:

- server: This directory contains the Flask app and its components, including the API, configuration, NLP model, memory manager, and automated training script.
- frontend1: This directory contains the frontend code for the chatbot interface.
- README.md: This file provides an overview of the project.
- LICENSE: This file contains the project's license.

### Back End
The back end of the AdventureBot project is built using Flask, a Python web framework. The back end consists of the following components:

- api: This directory contains the Flask routes for handling HTTP requests and responses.
- config: This directory contains the Flask configuration settings.
- nlu: This directory contains the NLP model for processing user inputs and generating responses.
- memory: This directory contains the memory manager for capturing and retaining information across interactions.
- tests: This directory contains the unit tests for the Flask app.
 -logs: This directory contains the log files for the Flask app.
- app.py: This file is the main entry point for the Flask app.
- requirements.txt: This file contains the required Python packages for the Flask app.

### API
The API of the AdventureBot project is built using Flask routes. The API consists of the following routes:

- /: This route serves the chatbot interface.
- /api/process: This route processes user inputs and generates responses.
- /api/memory: This route provides access to the chatbot's memory.

### Front End
The front end of the AdventureBot project is built using HTML, CSS, and JavaScript. The front end consists of the following files:

- index.html: This file is the main HTML file for the chatbot interface.
- style.css: This file contains the CSS styles for the chatbot interface.
- script.js: This file contains the JavaScript code for the chatbot interface.

## Usage

To use the AdventureBot chatbot, simply enter a message in the chatbot interface and press the "Send" button. The chatbot will process your message and generate a response. The chatbot's memory will be updated with any new information provided in the message.



## Secret sauce

AdventureBot consists of the following core components:

### TensorFlow Model (tf_model.py)

This component encapsulates your custom TensorFlow model. The model can be trained and fine-tuned on new data collected from user interactions or other sources. It has methods for loading and saving model checkpoints, generating responses, evaluating model performance, and querying ChatGPT when necessary.

## Active Selection
The YourTensorFlowModel class in tf_model.py has been updated to include active selection logic. This logic selects the best response from previous turns based on the chatbot model's score.

## Game-Related Responses
The YourTensorFlowModel class in tf_model.py has also been updated to include game-related responses. If the user wants to play a game, the chatbot generates a game-related response using the generate_game_response() method.

### NLP Model (nlp_model.py)

This component serves as the bridge between user inputs and the TensorFlow model or ChatGPT. It checks the confidence score of the TensorFlow model and decides whether to process the input using the TensorFlow model or fallback to ChatGPT.

### Memory Manager (memory_manager.py)

This component manages the memory of the chatbot, capturing and retaining information across interactions. It also collects new data for training and provides methods to access and update the memory.

### Automated Training Script (automated_training.py)

This script automates the process of collecting new data, training the TensorFlow model, and saving the updated model. This script can be set up to run periodically or triggered manually.

## Code Logic

### User Input Processing

User inputs are processed through the `NLPModel` class in `nlp_model.py`. The `process_user_input` method checks the confidence score of the TensorFlow model. If the confidence is high enough, it uses the TensorFlow model to generate a response; otherwise, it queries ChatGPT.

### Training and Fine-tuning

New data collected during user interactions is stored via the `MemoryManager`. The `automated_training.py` script retrieves new data, trains the TensorFlow model, and saves the updated model.

### Memory Management

Memory is managed through the `MemoryManager` class, which loads, updates, and saves memory data to a file.

### Evaluation and Self-improvement

The TensorFlow model's performance can be evaluated and compared to ChatGPT using the `evaluate` method in `tf_model.py`. The system is designed for continuous improvement through training on new data and self-evaluation.


