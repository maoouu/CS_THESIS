if [ -d "WEBSITE/.env" ]; then
    echo "A python virtual environment has already been created."
else
    cd WEBSITE/
    python3 -m venv .env
    source .env/bin/activate
    python3 -m pip install poetry
    poetry install

    echo "Successfully created python virtual environment."
fi