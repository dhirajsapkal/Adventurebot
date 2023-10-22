from server.nlu.tf_model import YourTensorFlowModel
from server.memory.memory_manager import MemoryManager

def automated_training():
    memory_manager = MemoryManager()
    tf_model = YourTensorFlowModel()

    new_data = memory_manager.get_new_data()
    if new_data:
        tf_model.train(new_data)
        tf_model.save_model()

# Set up a scheduler to run automated_training periodically, or run manually
