import json
import os

def load_json_data(file_path):
    """
    Fungsi untuk memuat data dari file JSON.
    
    Args:
        file_path (str): Path ke file JSON.
        
    Returns:
        list/dict: Data dari file JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} tidak ditemukan.")
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"File {file_path} tidak dapat dibaca. Error: {e}")
