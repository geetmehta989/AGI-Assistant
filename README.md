# Hackathon-AGI-Assistant

An AI-based desktop assistant that captures your screen, listens to your voice, extracts text, converts speech to text, and generates a structured JSON summary.

## Features

- 📸 Screen Capture: Takes screenshots of your screen
- 🎤 Voice Recording: Records audio input from your microphone
- 📝 OCR: Extracts text from screenshots using OCR
- 🗣️ Speech-to-Text: Converts audio to text using Vosk
- 📊 JSON Output: Generates structured JSON summaries

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

Or use the executable:
```bash
./dist/main.exe
```

## Build Executable

```bash
pyinstaller --onefile main.py
```

