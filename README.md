# RestokenAPI

## Running the app locally

### Requirements
This project was developed on WSL2 on top of Windows11:

* **OS:** Windows 11
* **WSL2 distribution:** Debian GNU/Linux 11 (bullseye)
* **Python:** 3.9.2
* **Pip:** 23.2.1

### First time setup instructions

```bash
# update stuff
$ sudo apt update && upgrade -y

# make sure python3 and pip are installed
sudo apt install python3 python3-pip

# install pipenv because it's much cooler than pip
$ pip install pipenv

# install postgresql database server
$ sudo apt install postgresql

# set a password for user postgres
$ sudo passwd postgres

# close and reopen the terminal
$ exit
```

### Running the app

```bash
# start postgresql service
$ sudo service postgresql start

# clone the repo
$ git clone https://github.com/bytefull/restoken-backend.git
$ cd restoken-backend

# create a virtual environment and activate it
$ pipenv shell

# install the required packages inside the virtual environment
$ pipenv install

# make other device on LAN able to see the app
$ netsh interface portproxy add v4tov4 listenport=8000 listenaddress=0.0.0.0 connectport=8000 connectaddress=172.30.15.113

# run the application
$ uvicorn restoken.app:app --reload --log-level debug --host 0.0.0.0
```

## The app is deployed on Azure [here](https://restoken.azurewebsites.net/docs)
Azure app service will internally use this command to run the app:

```bash
$ gunicorn restoken.app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --reload
```
