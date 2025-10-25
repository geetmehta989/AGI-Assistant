import tkinter as tk
from tkinter import ttk
import threading
from capture_module import capture_screen, record_audio
from speech_to_text import audio_to_text
from ocr_reader import extract_text_from_image
from data_handler import create_output_json, save_output_json, get_output_path

class AGIAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AGI Assistant")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(main_frame, text="🤖 AGI Assistant", font=("Arial", 20, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready to capture", font=("Arial", 12))
        self.status_label.pack(pady=10)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate', length=400)
        self.progress.pack(pady=10)
        
        # Start Capture button
        self.capture_btn = ttk.Button(main_frame, text="Start Capture", command=self.start_capture, width=30)
        self.capture_btn.pack(pady=10)
        
        # Exit button
        exit_btn = ttk.Button(main_frame, text="Exit", command=self.root.quit, width=30)
        exit_btn.pack(pady=10)
        
        # Info text
        info_text = "Click 'Start Capture' to capture your screen,\nrecord audio, and generate a JSON summary."
        info_label = ttk.Label(main_frame, text=info_text, font=("Arial", 9), justify=tk.CENTER)
        info_label.pack(pady=20)
    
    def start_capture(self):
        """Start the capture process in a separate thread"""
        self.capture_btn.config(state='disabled')
        self.status_label.config(text="Processing...")
        self.progress.start()
        
        # Run capture in a separate thread to avoid freezing the UI
        thread = threading.Thread(target=self.capture_process)
        thread.daemon = True
        thread.start()
    
    def capture_process(self):
        """Execute the complete capture process"""
        try:
            # Step 1: Capture screen
            self.update_status("Capturing screen...")
            capture_screen()
            
            # Step 2: Record audio
            self.update_status("Recording audio (10 seconds)...")
            record_audio(duration=10)
            
            # Step 3: Extract text from screenshot
            self.update_status("Extracting text from screenshot...")
            screen_text = extract_text_from_image()
            
            # Step 4: Convert audio to text
            self.update_status("Converting speech to text...")
            speech_text = audio_to_text()
            
            # Step 5: Create and save JSON
            self.update_status("Creating output JSON...")
            output_data = create_output_json(speech_text, screen_text)
            save_output_json(output_data)
            
            # Step 6: Get output path
            output_path = get_output_path()
            
            # Step 7: Complete
            self.update_status("Task Completed!")
            self.root.after(0, lambda: self.show_completion(output_path))
            
        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            self.root.after(0, self.enable_capture)
    
    def update_status(self, text):
        """Update status label (thread-safe)"""
        self.root.after(0, lambda: self.status_label.config(text=text))
    
    def show_completion(self, output_path):
        """Show completion message"""
        self.progress.stop()
        self.status_label.config(text=f"Task Completed!\nOutput: {output_path}")
        self.enable_capture()
    
    def enable_capture(self):
        """Re-enable the capture button"""
        self.capture_btn.config(state='normal')

def run_app():
    root = tk.Tk()
    app = AGIAssistantApp(root)
    root.mainloop()

