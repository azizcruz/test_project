# Presrequests
* Make sure docker and doker-compose is installed in your machine.
* Make sure python3.6 is installed.

# Installation
* navigate to your directory where you want the project folder to be.
* create a virtual environment using the following command
'''shell
$ python3 -m venv oculyze
'''
* navigate to oculyze directory
'''shell 
$ cd oculyze
'''
* activate the virtual environment
'''shell
$ source bin/activate
'''
* clone the project from the repo using the following command
'''shell
$ git clone https://github.com/azizcruz/test_project.git
'''
* when the project is cloned navigate to the directory
'''shell 
$ cd test_project
'''
* build the containers using docker-compose
'''shell
$ docker-compose build 
'''
this step may take some time to finish.
* when it is finished start the containers using
'''shell
$ docker-compose up 
'''
now both of the services are running and connected to a private network named test_project_private-net using docker bridge networks.

# Usage
* open your browser and paste in the search bar.
http://0.0.0.0:5000
this will redirect you to the endpoint where you can add data.