# file_handling.py
import os
from config import ALLOWED_EXTENSIONS
from pydub import AudioSegment


def file_is_allowed(filename) -> bool:
    """
    This function checks if the specified file is allowed.
    Allowed extensions are specified via ALLOWED_EXTENSIONS in config.py.

    Parameter:
    - filename (str): The name of the file

    Returns:
    bool: True if file is allowed; otherwise false
    """
    _, file_extension = os.path.splitext(filename)
    if not file_extension:
        return False
    return file_extension in ALLOWED_EXTENSIONS


def convert_mp3_to_wav(filepath) -> str:
    """
    This function takes a specified .mp3 file 
    and converts it to .wav. It returns the converted file path.

    Parameter:
    - filepath (str): The specified path to .mp3 file

    Returns:
    str: The converted file path
    """
    audio = AudioSegment.from_mp3(filepath)
    directory = os.path.dirname(filepath)
    wav_filename = os.path.basename(filepath).replace('.mp3', '.wav')
    output = os.path.join(directory, wav_filename)
    audio.export(output, format='wav')
    os.remove(filepath)
    return output