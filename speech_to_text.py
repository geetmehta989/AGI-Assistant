import json
import wave
from vosk import Model, KaldiRecognizer
import os

def init_vosk_model():
    """Initialize Vosk model"""
    model_path = "model"
    
    # Check if model exists, if not, create a note about downloading it
    if not os.path.exists(model_path):
        print("⚠ Vosk model not found. Please download a model from https://alphacephei.com/vosk/models")
        print("For English (small model): https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip")
        print("Extract the model to a 'model' directory in the project root.")
        return None
    
    try:
        model = Model(model_path)
        return model
    except Exception as e:
        print(f"Error loading Vosk model: {e}")
        return None

def audio_to_text(audio_file="audio.wav"):
    """Convert audio file to text using Vosk"""
    model = init_vosk_model()
    
    if model is None:
        return "Error: Vosk model not found. Please install the model."
    
    try:
        # Open audio file
        wf = wave.open(audio_file, "rb")
        
        # Check if audio file is valid
        if wf.getnchannels() != 1 or wf.getcomptype() != "NONE":
            print("Error: Audio file must be WAV format mono PCM.")
            return "Error: Invalid audio format"
        
        # Initialize recognizer
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)
        
        # Process audio
        text_parts = []
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text_parts.append(result.get('text', ''))
        
        # Get final result
        final_result = json.loads(rec.FinalResult())
        text_parts.append(final_result.get('text', ''))
        
        wf.close()
        
        # Combine all text parts
        full_text = ' '.join(text_parts).strip()
        
        if full_text:
            print(f"✓ Speech-to-text conversion successful")
            return full_text
        else:
            print("No speech detected in audio")
            return "No speech detected"
            
    except Exception as e:
        print(f"Error during speech-to-text conversion: {e}")
        return f"Error: {e}"

