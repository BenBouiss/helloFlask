git repos for the "étude de cas" course

# Installation et utilisation de pyenv

- $ pyenv install 3.8.6
- $ pyenv local 3.8.6


# Installation et utilisation de Poetry

Install pipx
```bash
sudo apt get pipx
```

Install Poetry 
```bash
pipx install poetry
```

Verification
```bash
poetry --version
```

Init poetry in directory
```bash
poetry new folder\_name
poetry add file\_name
```

Install and run app
```bash
poetry install
poetry run folder\_lib\_name:function \*\*arg
```

Build and install lib
```bash
poetry build
```
Creates a "dist" folder with an archive .gz and a .whl file. pip install said file to install the lib to virt env.



# Installation et utilisation de Docker





Build and run the docker
```bash
sudo docker build -t app\_flask .
sudo docker run -p 8000:5000 app\_flask
```

Builds the docker using the Dockerfile present then runs it forwarding the 5000 port used by default by Flask to the 8000 port.
