if [ -d "WEBSITE/.env" ]; then
    echo "A python virtual environment has already been created."
else
    cd WEBSITE/
    sudo apt install python3-pip
    sudo apt install python3.10-venv
    echo "Successfully created python virtual environment."
    python3 -m venv .env
fi
cd WEBSITE/
source .env/bin/activate
python3 -m pip install poetry
poetry install
python3 model.py
echo "Use the command 'python3 app.py' to run the website."