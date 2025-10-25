import mss
import sounddevice as sd
import wave
import numpy as np
from datetime import datetime

def capture_screen():
    """Capture a screenshot of the screen and save it as screenshot.png"""
    try:
        with mss.mss() as sct:
            # Capture the entire screen
            screenshot = sct.grab(sct.monitors[1])
            
            # Convert to numpy array and save as PNG
            img = np.array(screenshot)
            img_rgb = img[:, :, [2, 1, 0]]  # BGR to RGB conversion
            
            from PIL import Image
            img_pil = Image.fromarray(img_rgb)
            img_pil.save("screenshot.png")
            print("✓ Screenshot captured and saved as screenshot.png")
            return True
    except Exception as e:
        print(f"Error capturing screen: {e}")
        return False

def record_audio(duration=10, sample_rate=16000):
    """Record audio from microphone for specified duration and save as audio.wav"""
    try:
        print(f"Recording audio for {duration} seconds...")
        # Record audio
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()  # Wait until recording is finished
        
        # Convert to int16
        audio_data = (audio_data * 32767).astype(np.int16)
        
        # Save as WAV file
        with wave.open("audio.wav", "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.tobytes())
        
        print("✓ Audio recorded and saved as audio.wav")
        return True
    except Exception as e:
        print(f"Error recording audio: {e}")
        return False

