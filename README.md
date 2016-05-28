# Microservice example project using Python, RabbitMQ, Nameko and Flask

This a simple microservice sale and stock management system using Python, RabbitMQ, Nameko and Flask.  
It's just an example, where I demonstrate the use of these technologies.

## Build and Run ##

### Requirements ###
* Python 3.5.1
* Docker
  
### Run ###
* Download RabbitMQ Docker image:
```shell
docker run -d --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```
You can see RabbitMQ dashboard in http://192.168.99.100:15672

* Install Nameko and Flask
```shell
pip install nameko
pip install flask
```

* Run service
```shell
nameko run service --broker amqp://guest:guest@192.168.99.100
```

You can test the service by nameko shell:
```shell
nameko shell --broker amqp://guest:guest@192.168.99.100
n.rpc.sale.sell(1)
```

* Run api
```shell
python api.py
```

The api is avaible in http://localhost:5000/
  
#### License ####

The codebase is licensed under [GPL v3.0](http://www.gnu.org/licenses/gpl-3.0.html).
