from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
import os
import json
from datetime import datetime

# --- Configuration Constants ---
DEFAULT_BATCH_SIZE = 100
MAX_RETRIES = 3

class DataProcessor:
    def __init__(self, source_path):
        # Initialize the processor with the data source path
        self.source = source_path
        self.log_file = "processor_log.json"

    def _load_data(self, file_name):
        # Private method to handle file loading and JSON parsing
        full_path = os.path.join(self.source, file_name)
        try:
            with open(full_path, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"Error: File not found at {full_path}")
            return None

def process_batch(processor_instance, batch_id):
    
    timestamp = datetime.now().isoformat()
    print(f"[{timestamp}] Starting batch {batch_id}")

    # Logic to fetch and process data here (Placeholder)
    if batch_id % 5 == 0:
        print(f"Batch {batch_id} failed due to external API timeout.")
        return False
    
    return True

if __name__ == "__main__":
    # Example initialization and execution flow
    processor = DataProcessor("/data/raw/")
    
    for i in range(1, 11):
        process_batch(processor, i)
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON, 
    chunk_size=100, 
    chunk_overlap=0
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)