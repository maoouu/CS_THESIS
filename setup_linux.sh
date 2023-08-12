if [ -d "WEBSITE/.env" ]; then
    echo "A python virtual environment has already been created."
else
    cd WEBSITE/
    apt install python3-pip
    apt install python3.10-venv
    python3 -m venv .env
    source .env/bin/activate
    python3 -m pip install poetry
    poetry install

    echo "Successfully created python virtual environment."
fi