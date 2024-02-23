git repos for the "étude de cas" course

# Installation et utilisation de pyenv
```bash
pyenv install 3.8.6
pyenv local 3.8.6
```

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
poetry new folder_name
poetry add file_name
```

Install and run app
```bash
poetry install
poetry run folder_lib_name:function **arg
```

Build and install lib
```bash
poetry build
```
Creates a "dist" folder with an archive .gz and a .whl file. pip install said file to install the lib to virt env.



# Installation et utilisation de Docker





Build and run the docker
```bash
sudo docker build -t app_flask .
sudo docker run -p 8000:5000 app_flask
```

Builds the docker using the Dockerfile present then runs it forwarding the 5000 port used by default by Flask to the 8000 port.

Remove dangling(< none >) images
```bash
sudo docker rmi $(docker images -f "dangling=true" -q)
```

Stop and delete all active containers
```bash
docker stop $(docker ps -a -q)
docker rm $ (docker ps -a -q) 
```

# Utilisation de postgres




Launch postgres docker image at the port 5455 redirecting to 5432
```bash
docker run --name myPostgresDb -p 5455:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=BenBouiss -e POSTGRES_DB=visiteur_count -d postgres
```
Use with DBeaver instanciate server using localhost:5455 and tick show all database




