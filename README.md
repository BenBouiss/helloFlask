git repos for the "étude de cas" course

# Installation et utilisation de pyenv

- $ pyenv install 3.8.6
- $ pyenv local 3.8.6


# Installation et utilisation de Poetry

Install pipx
- $ sudo apt get pipx

Install Poetry 
- $ pipx install poetry

Verification
- $ poetry --version

Init poetry in directory
- $ poetry new folder\_name
- $ poetry add file\_name

Install and run app
- $ poetry install
- $ poetry run folder\_lib\_name:function \*\*arg

Build and install lib
- $ poetry build
Creates a "dist" folder with an archive .gz and a .whl file. pip install said file to install the lib to virt env.
