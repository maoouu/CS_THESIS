if [ -d "WEBSITE/.env" ]; then
    echo "A python virtual environment has already been created."
else
    cd WEBSITE/
    sudo apt install python3-pip
    sudo apt install python3.10-venv
    sudo apt install ffmpeg
    python3 -m venv .env
    source .env/bin/activate
    python3 -m pip install poetry
    poetry install
    python3 model.py
    echo "Successfully created python virtual environment."
    echo "Use the command 'python3 app.py' to run the website."
fi