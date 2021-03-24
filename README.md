# Azure App Services +  Flask + Postgres V0.5


This in an app, that has an almost complete pipeline. The principal goal is making a FLASK served frontend that allows you
to put your e-mail and recieve some information (via e-mail) from a Postgres Database hosted in a Virtual Machine deployed by ansible.
The github actions pipeline is configured that each commit you will Run the Jobs and Deploy to azure web services 

### Requeriments 📋

- Ansible ☄️
- Python 🐍
- Azure Cloud access ☁️ : Virtual Machine & Az App services

### Used tech 👨‍💻

- **Ansible** ☄️
- **Python** 🐍
- **Pytest** 📈
- **Flask** ⚗️

### Libraries  📒 - Requeriments.txt

```
Flask==1.1.2
pytest==6.2.2
psycopg2==2.8.6
python-dotenv==0.15.0
prettytable==2.1.0
py3-validate-email==1.0.0
```
### List of Routes 📖 

| Version | Route | Behavior|
| ----------- | ----------- | -----------
| 0.1| / |  Render the template index.html | 
| 0.5 | /logs | Streams the logs from THE FLASK server |

### Secrets  🤫

Inside the secrets folders you should create your `.env` with this variables:
```
PSQL_HOST= Your virtual machine IP host
PSQL_DATABASE= You can let default postgres or use the one that you will create in ANSIBLE-PLAYBOOK
PSQL_USER= You can let default postgres or use the one that you will create in ANSIBLE-PLAYBOOK
PSQL_PASS= The user password created with ANSIBLE-PLAYBOOK
MAIL= Your testing mail adress to send python emails (Access to less secure apps activated)
MAIL_PASS= The password of your testing mail
```
### Setting up the PSQL database  in a Virtual Machine with ansible! 🖥️

##### Create the inventory ( or hostfile )  📂

Inside the ansible folder you can create your inventory file: 

**host.yml** 📜
```
[azure-web-ser]
IpAdress-of-your-VM

# Local variables for Ansible playbooks
[azure-web-ser:vars]
ansible_ssh_user=Your VM username
ansible_ssh_pipelining= true
ansible_python_interpreter=/usr/bin/python3
PSQL_USER= New username of postgresql 
PSQL_PASS=New pass of postgresql 
```


Inside the ansible folder you can simply modify and execute the `run.sh`  📂


``` 
sudo ansible-playbook deploy.yml -i host.yml --key-file ~/.ssh/Yourkey -vvv 
```

After all that, your PostgresSQL should be installed and running in your VM, just dont forget to modify your
Postgres config files  : ⚙️ 

 ```  
 # modify conf string
  sudo vim /etc/postgresql/10/main/pg_hba.conf 
 
   host    all    all    10.0.0.0/16    md5
```

And modify your ` postgresql.conf` ⚙️
```
 sudo vim /etc/postgresql/10/main/postgresql.conf
```

In authentication and connection server: **`listen_addresses="*"`**



### Populate your database with dummy data 📝⚙️📋 :

Inside the server folder, there are some functions that generate random names and scores to populate your Database, you can call the function from your main.py or app.py 

 ```
#Loop and populate the db with 10 entries
  for i in range(10):
     populate_db("score") 
```

### Launch your FLASK server! ⚗️👥

You just have to run the app.py located in the root directory, he is going to import the app function from client/index.py
``` 
flask run
```

### ☁️☁️ Deploy in the CI/CD of Azure ☁️☁️

in the folder `.github/workflows` there is the `main_app.yml` file 

To get your own .yml action jobs file, log into your webservice and connect your github account. Azure is going to make a secret in your repository


name: Build and deploy Python app to Azure Web App - Jojapp
```
publish-profile: ${{ secrets.AzureAppService_PublishProfile_8fb896a1938b427d822d3f4e0db68b1a }} 
```

Then you just have to modify this file `main_app.myml` , with your own secret name, and thats it.

**Have fun!** 👾👽
 