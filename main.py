import speech_recognition as sr
from pydub import AudioSegment
import os

def transcribe_mp3(file_path):
    # 1. Define filenames
    # We create a temporary wav file because SpeechRecognition doesn't read mp3
    temp_wav = "temporary_conversion.wav"

    try:
        # 2. Convert MP3 to WAV
        print(f"--- Converting {file_path} to WAV format ---")
        audio = AudioSegment.from_mp3(file_path)
        audio.export(temp_wav, format="wav")

        # 3. Initialize the Recognizer
        recognizer = sr.Recognizer()

        # 4. Load and Process the Audio
        with sr.AudioFile(temp_wav) as source:
            print("Cleaning up background noise...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            print("Transcribing audio (this may take a moment)...")
            audio_data = recognizer.record(source)

        # 5. Convert Audio to Text using Google's Engine
        # You can change language='en-US' to other codes like 'es-ES' or 'fr-FR'
        text = recognizer.recognize_google(audio_data, language='en-US')
        
        print("\n--- Transcription Successful ---")
        return text

    except sr.UnknownValueError:
        return "Error: Google Speech Recognition could not understand the audio."
    except sr.RequestError as e:
        return f"Error: Could not request results from Google service; {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
    finally:
        # 6. Cleanup: Remove the temporary WAV file
        if os.path.exists(temp_wav):
            os.remove(temp_wav)
            print("--- Temporary files cleaned up ---")

# --- EXECUTION ---
if __name__ == "__main__":
    # Replace 'my_audio.mp3' with the actual name of your file
    input_file = r"D:\AudiReading\voicebosch-countdown-from-10-190389.mp3" 
    
    if os.path.exists(input_file):
        result = transcribe_mp3(input_file)
        print("\nRESULT:\n", result)
        
        # Optional: Save the result to a text file
        with open("transcription_output.txt", "w") as f:
            f.write(result)
    else:
        print(f"Error: The file '{input_file}' was not found in this folder.")
