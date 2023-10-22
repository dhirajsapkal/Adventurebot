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


## Core Components

AdventureBot consists of the following core components:

### TensorFlow Model (tf_model.py)

This component encapsulates your custom TensorFlow model. The model can be trained and fine-tuned on new data collected from user interactions or other sources. It has methods for loading and saving model checkpoints, generating responses, evaluating model performance, and querying ChatGPT when necessary.

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

## Usage

```python
# Instantiate the NLP model
nlp_model = NLPModel()

# Process a user input
response, memory_update = nlp_model.process_user_input("Hello!", {})