🎙️ Speech-To-Text (Audio File Based) – Python Project
📌 Project Overview

This project is a file-based Speech-to-Text system developed using Python. It converts pre-recorded audio files (MP3 format) into readable text using the Google Speech Recognition engine.

The system automatically:
  Converts MP3 files to WAV format
  Processes and transcribes the audio
  Handles errors efficiently
  Deletes temporary files after processing
  Saves the final transcription into a text file

🚀 Features
Convert MP3 audio files to text
Automatic MP3 → WAV conversion
Background noise adjustment
Error handling for recognition failures
Saves output to transcription_output.txt
Automatic cleanup of temporary files

🛠️ Technologies Used
Python 3
SpeechRecognition
pydub
Google Speech Recognition API
OS module

📂 Project Structure
Speech-To-Text-Project/
│
├── main.py
├── transcription_output.txt
└── README.md
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/Speech-To-Text-Project.git
cd Speech-To-Text-Project
2️⃣ Install Required Libraries
pip install SpeechRecognition
pip install pydub

⚠️ Important:
You must install FFmpeg for MP3 conversion to work.

Download from:
https://ffmpeg.org/download.html

After installation, add FFmpeg to your system PATH.

▶️ How to Run
Place your MP3 file inside the project folder.

Update this line in the script:
input_file = r"your_audio_file.mp3"

Run the program:
python main.py

The transcription will:
Display in the terminal

Be saved in transcription_output.txt

🌎 Language Support
Change language by modifying:
recognizer.recognize_google(audio_data, language='en-US')
Examples:
'en-US' → English

❗ Error Handling
The program handles:
Unrecognized speech
API request failures
Missing audio file
Unexpected runtime errors

📌 Future Improvements
Support multiple audio formats
Add GUI interface
Batch file processing
Offline speech recognition
Web-based version

👨‍💻 Author
Developed as a Python project for learning speech recognition and audio processing.
