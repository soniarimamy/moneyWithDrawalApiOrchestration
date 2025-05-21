# **RUN MONEY WITHDRAW ORCHESTRATION API IN LOCAL SERVER**

Hi lads!, this tutorial guides you, step by step, how to run moneyWithDrawOrchestration api in your local machine</br>

### **Step I - PREREQUISITES**</br>

- Python<=3.11 and >=3.7, already installed in your machine - [Compulsory]</br>

  > Link: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu

- Pycharm Or Visual Studio Code IDE [Optional]</br>

  > Link: https://linuxconfig.org/how-to-install-pycharm-on-ubuntu-20-04-linux-desktop

- Docker, already installed in your machine[Optinal]</br>

  > Link: https://www.cherryservers.com/blog/how-to-install-and-start-using-docker-on-ubuntu-20-04

- Docker-compose, installed and configured in your local machine [Optinal]</br>

  > Link: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04

- Unix Operating System, installed in real machine [Ubuntu, Debian, Kali, etc...]</br>

  > Link: https://phoenixnap.com/kb/install-ubuntu-20-04

- Postgresql database and pgAdmin dashboard already installed [Compulsory]</br>
  > Link: https://vitux.com/how-to-install-postgresql-and-pgadmin4-on-ubuntu/

### **Step II - RUN MONEY WITHDRAW ORCHESTRATION API**</br>

a) First of all, you should download this code in gitlab by typing this command in your terminal: :airplane:</b>

> git clone --branch production https://github.com/soniarimamy/moneyWithDrawalApiOrchestration.git </b>

b) Then go do inside moneyWithDrawalApiOrchestration/ folder and install all python requirements

> cd moneyWithDrawalApiOrchestration/ </b>

> pip3.11 install virtualenv </b>

> python3.11 -m virtualenv env </b>

> source env/bin/activate </b>

> pip3 install -r requirements.txt </b>

c-1) type the below command to run directly the app

> python3 moneyWithdrawalApiOrchestration-core.py

### **Step III - TEST MONEY WITHDRAW ORCHESTRATION API**</br>

a) To test opencrvs moneyWithDrawOrchestration api, check the swagger in this url:

> http://<your_server_ip>:<6009>/bank/docs </br>

b) Click "_**Send button**_" to launch each web services you want to execute and see the results.</br>

### => Now you have configured, launched, and tested moneyWithDrawOrchestration api, **_Congratulations!_** :smiley:
