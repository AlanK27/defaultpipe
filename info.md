



### Intro


### Components

In order to use celery which spins up multi thread to process task asyncronizely we need a memory cache/broker, there are many but redis will do for now. 
Broker can only be evoked through docker so a container has to be ran. Local Redis is initialized in the `supervisord.conf` file 


Refer to different brokers
https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/index.html




### Reference

https://medium.com/swlh/python-developers-celery-is-a-must-learn-technology-heres-how-to-get-started-578f5d63fab3

Connecting Celery, Flask, and Redis
https://signoz.io/blog/celery-worker/

