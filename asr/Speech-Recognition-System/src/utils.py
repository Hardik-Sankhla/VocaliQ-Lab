import soundfile as sf
import numpy as np

def process_audio(audio_file_path):
    """
    Loads an audio file and performs basic preprocessing.

    Args:
        audio_file_path (str): Path to the audio file.

    Returns:
        tuple: (audio_data, samplerate) as a numpy array, or (None, None) on error.
    """
    try:
        audio_data, samplerate = sf.read(audio_file_path)
        print(f"Loaded audio file: {audio_file_path}, Samplerate: {samplerate}")

        # Ensure audio_data is 1D (mono)
        if audio_data.ndim > 1:
            audio_data = audio_data[:, 0]  # Take the first channel
            print("Converted audio to mono.")
        return audio_data, samplerate
    except sf.LibsndfileError as e:
        print(f"Error reading audio file: {e}")
        return None, None
    except FileNotFoundError:
        print(f"Error: Audio file not found at {audio_file_path}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred while processing audio: {e}")
        return None, None
