import json
from datetime import datetime

def create_output_json(speech_text, screen_text):
    """Create structured JSON output with speech and screen text"""
    data = {
        "speech_text": speech_text,
        "screen_text": screen_text,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return data

def save_output_json(data, output_file="output.json"):
    """Save data to JSON file"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✓ Output saved to {output_file}")
        return True
    except Exception as e:
        print(f"Error saving output file: {e}")
        return False

def get_output_path(output_file="output.json"):
    """Get the full path of the output file"""
    import os
    return os.path.abspath(output_file)

