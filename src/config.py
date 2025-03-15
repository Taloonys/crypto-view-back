import os


API_KEY: str


api_key_file = os.getenv('API_KEY_FILE', 'r')
if not api_key_file: 
    raise ValueError("API_KEY_FILE env variable")

try:
    """
    Char OS (File generated in Unix)
    """
    with open(api_key_file, 'r', encoding='utf-8') as f:
            API_KEY = f.read().strip()
except UnicodeDecodeError:
    """
    Wide-char OS (File generated in Windows)
    """
    with open(api_key_file, 'r', encoding='utf-16') as f:
        API_KEY = f.read().strip()