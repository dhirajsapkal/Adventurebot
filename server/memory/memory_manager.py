import json
import os

class MemoryManager:
    _instance = None  # Class variable to hold the singleton instance

    def __new__(cls, *args, **kwargs):
        # Override __new__ to implement the Singleton pattern
        if not cls._instance:
            cls._instance = super(MemoryManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, memory_file='memory.json'):
        self.memory_file = memory_file  # File path for saving memory data
        self._load_memory()  # Load existing memory data from file

    def _load_memory(self):
        """Load memory data from file."""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as file:
                    self.memory = json.load(file)
            except Exception as e:
                print(f"Failed to load memory: {e}")
                self.memory = {}  # Default to empty dict if loading fails
        else:
            self.memory = {}  # Default to empty dict if file doesn't exist

    def get_memory(self):
        """Get the current memory data."""
        return self.memory

    def update_memory(self, memory_update):
        """
        Update memory data with the provided dictionary.
        
        Parameters:
        memory_update (dict): Dictionary with data to update memory.
        """
        self.memory.update(memory_update)
        self._save_memory()  # Save updated memory data to file

    def _save_memory(self):
        """Save current memory data to file."""
        try:
            with open(self.memory_file, 'w') as file:
                json.dump(self.memory, file, indent=4)
        except Exception as e:
            print(f"Failed to save memory: {e}")

    def reset_memory(self):
        """Reset memory data to an empty dictionary and delete memory file."""
        self.memory = {}
        try:
            os.remove(self.memory_file)
        except Exception as e:
            print(f"Failed to reset memory: {e}")

    def update_training_status(self, status):
        """
        Update the training status of the TensorFlow model in memory.
        
        Parameters:
        status (dict): Dictionary with training status data.
        """
        self.memory['training_status'] = status
        self._save_memory()  # Save updated training status to file

    def collect_new_data(self, user_input, model_response):
        # Collect new data for training
        pass

    def get_new_data(self):
        # Retrieve collected new data for training
        pass

# Usage:
# memory_manager = MemoryManager()
# memory_manager.update_training_status({'is_trained': True, 'last_trained': '2023-10-21'})
