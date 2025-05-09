# Text-to-Speech Synthesis

## Overview

Text-to-Speech (TTS) synthesis is the process of converting written text into spoken words. This technology has a wide range of applications, including virtual assistants, assistive technologies, audiobooks, and more. This project demonstrates a basic TTS system using the Google Text-to-Speech (gTTS) library, which converts input text into speech and generates audio files that can be played back.

## About gTTS

The gTTS (Google Text-to-Speech) library is a Python-based tool that provides an interface to Google Translate's text-to-speech API. It supports multiple languages, allows control over speech speed, and enables the conversion of text into spoken audio, which can be saved as MP3 files or used in real-time applications.

## Features

- **Multi-language Support**: Convert text to speech in various languages.
- **Audio File Generation**: Save the generated speech as an MP3 file.
- **Playback Capability**: Play the generated audio file directly from the script.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone <repository_url>
    cd Text-to-Speech-Synthesis
    ```

2. **Install Dependencies**:

    Ensure you have Python installed. Then, install the required Python packages:

    ```bash
    pip install gtts
    ```

## Usage

### Example Script

Below is an example of how to use the gTTS library to convert text to speech:

```python
from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3'):
    """
    Convert text to speech and save the output as an audio file.
    :param text: Text to convert to speech
    :param language: Language for speech synthesis (default is English)
    :param output_file: The name of the output audio file
    """
    # Initialize gTTS object with text and language
    tts = gTTS(text=text, lang=language, slow=False)  # slow=False makes the speech faster

    # Save the generated speech to an audio file
    tts.save(output_file)
    print(f"Speech saved as {output_file}")

    # Play the generated speech (optional)
    if os.name == 'nt':  # For Windows
        os.system(f"start {output_file}")
    elif os.name == 'posix':  # For macOS/Linux
        os.system(f"afplay {output_file}" if os.uname().sysname == 'Darwin' else f"mpg321 {output_file}")

# Example usage
if __name__ == "__main__":
    text = "Hello, welcome to the Text-to-Speech project. I hope you enjoy learning!"
    text_to_speech(text)  # Convert the text to speech and save as 'output.mp3'
```

### Running the Script

1. Navigate to the project directory:

    ```bash
    cd src
    ```

2. Run the script:

    ```bash
    python text_to_speech.py
    ```

3. Enter the text you want to convert to speech when prompted. For example:

    ```plaintext
    Enter the text you want to convert to speech: Hello! Welcome to the Text-to-Speech program.
    ```

    The generated speech will be saved as `output.mp3` and played back automatically.

## Example Output

```plaintext
Enter the text you want to convert to speech: Hello! My name is Hardik Sankhla. Welcome to my introductory script, generated using the Text-to-Speech program by Vocal I Q Lab. Enjoy the demonstration.
Speech saved as output.mp3
```

<audio controls>
  <source src="https://github.com/Hardik-Sankhla/Markdown-Resources/raw/main/Audio/intro.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

## Notes

- The default language is English (`en`). To use a different language, modify the `language` parameter (e.g., `'es'` for Spanish, `'de'` for German).
- Ensure you have the necessary audio playback tools installed on your system for the `os.system` command to work.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/) for providing the core functionality.
- Vocal I Q Lab for supporting this project.

---

Enjoy exploring Text-to-Speech synthesis with this project!
