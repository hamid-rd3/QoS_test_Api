
<p align="center">
  <img  src="https://user-images.githubusercontent.com/87657199/186894836-498ce9df-360e-439f-8f0c-e8a2128dc09a.png">
</p>



--------------------------------------------------------------------------------

In this repo I create a REST API and implement some qos tests to measure quality of service parameters such as packet loss http responce jitter... 

<!-- toc -->

- [More about QoS parameters](#More-about-QoS-parameters)
- [Beginner Installation](#Beginner-Installation)
-   [Create your virtual environment](#Create-your-virtual-environment)
-   [Add an admin user](#Add-an-admin-user)
-   [Launch the api](#Launch-the-api)
- [Swagger redoc](#Swagger-redoc)

<!-- tocstop -->

## More about QoS parameters


<p align="center">
  <img  src="https://user-images.githubusercontent.com/87657199/186893731-615227d7-936b-435d-b9e9-562a3d1c8323.png">
</p>


more Information about Selenium and How To Measure Page Load Times  :

  " https://www.lambdatest.com/blog/how-to-measure-page-load-times-with-selenium/ "
  
  "https://www.w3.org/TR/navigation-timing-2/#dfn-redirect-count"
  
How to use ping command to extract packet loss jitter and latency :

  "https://linux.die.net/man/8/ping"
  
source code and a guide to ddosify :

  "https://github.com/ddosify/ddosify"
  
How to use cURL and an Introduction to HTTP Transaction Timing :

  " https://netbeez.net/blog/http-transaction-timing-breakdown-with-curl"

optimization api performance with the help of asyncio and multi-threading  :

"https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor"


 

## Beginner Installation

### Create your virtual environment

"you may want to install python 3.8+ and pip package on linux kernel or WSL before starting Installation"
 
**On Linux or WSL**
```bash
pip install virtualenv
python3 -m venv .venv
source .venv/bin/activate 
#to ensure your environment activation you can check by :
which python
```
**Install the requirement packeges**
```bash
pip install -r requirements.txt
chmod +x install_required.sh
./install_required.sh
```
### Add an admin user


**Admin and create QoS objects**
```bash
cd backend 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
##Register with your desired username and password

```
**Start server**
```bash
#default port 8000 select another port if you want   
python manage.py runserver 8000
```
### Launch the api

In here the goal is to simulate a client using the api  

Open another bash :

```bash
#bash 2
source .venv/bin/activate
cd py_client
#Configure your qos input arguments in config.yaml
#login to your super-user account 
python create.py

```
you can open your browser to see the views 

url patterns :
```bash
#http://localhost:8000/ +
1 admin/
2 api/
3 api/ auth/
4 api/ swagger-json/ [name='schema-json']
5 api/ swagger/ [name='schema-swagger-ui']
6 api/ redoc/ [name='schema-redoc']
7 api/ get-details
8 api/ api-register
9 api/products/ <int:pk>/
10 api/products/
11 api/products/ <int:pk>/update/
12 api/products/ <int:pk>/delete/
```

![image](https://user-images.githubusercontent.com/87657199/188329748-3df93789-fac2-47f9-98b4-ec84237e62d1.png)


## Swagger redoc

if server is running you can see the swagger redoc document below 

" http://185.130.78.174:5201/api/redoc/ "

offline redoc document

[QoS API Doc.pdf](https://github.com/hamid-rd3/QoS_test_Api/files/9485327/QoS.API.Doc.pdf)


Good Luck 👍

