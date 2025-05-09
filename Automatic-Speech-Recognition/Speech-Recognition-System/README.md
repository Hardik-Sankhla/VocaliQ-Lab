# Basic Speech Recognition System

This project implements a basic speech recognition system using Python and the SpeechRecognition library. It captures audio from the microphone or reads from an audio file and transcribes it into text using the Google Speech Recognition API.

## Features

* Captures audio from the default microphone.
* Reads audio from a WAV file.
* Uses the Google Speech Recognition API for transcription.
* Prints the transcribed text to the console.
* Handles errors for unknown audio and API request failures.
* Includes utility functions for audio processing.
* Provides a Jupyter Notebook demonstration.
* (Optional) Includes a Gradio/Streamlit demo application.

## Prerequisites

* Python 3.x
* SpeechRecognition library
* PyAudio library (and its system dependencies)
* soundfile library

## Installation

1. Clone this repository:

    ```bash
    git clone <repository_url>
    cd SpeechRecognitionSystem
    ```

2. Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate # On macOS and Linux
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Install PyAudio. This often requires system-level dependencies. See the PyAudio installation instructions for your operating system: [PyAudio Installation Instructions](https://pypi.org/project/PyAudio/)

    On Windows, you might need: `pip install PyAudio`

    On Ubuntu/Debian:

    ```bash
    sudo apt-get update
    sudo apt-get install libportaudio2 libportaudiocpp0 libportaudio-dev
    pip install PyAudio
    ```

## Usage

1. Run the ASR script:

    ```bash
    python src/asr.py
    ```

2. Speak into your microphone when prompted, or ensure that `samples/input_audio.wav` exists.
3. The transcribed text will be displayed in the console.

4. Demo Script (demo/main.py):

    ```bash
    python demo/main.py
    ```

5. Notebook Demo (notebooks/demo.ipynb):

    - Open the Jupyter notebook `notebooks/demo.ipynb`.
    - The notebook runs ASR on a sample audio file and displays the transcribed text.

6. Demo App (demo/app.py):

    ```bash
    python demo/app.py
    ```

## Code Structure

* `README.md`: This file (project documentation).
* `requirements.txt`: Lists the Python packages required for the project.
* `src/asr.py`: Contains the main Python script for speech recognition.
* `src/utils.py`: Contains utility functions.
* `notebooks/demo.ipynb`: A Jupyter Notebook demonstrating the system.
* `samples/input_audio.wav`: An example audio file.
* `samples/expected_output.txt`: The expected transcription of the example audio file.
* `demo/app.py`: (Optional) A Gradio/Streamlit application for a live demo.

