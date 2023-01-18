from config import ALLOWED_EXTENSIONS

# Check if filename is wav or mp3
def is_allowed_file_extension(filename):
    file_extension = filename.split('.')[-1].lower()
    return file_extension in ALLOWED_EXTENSIONS
