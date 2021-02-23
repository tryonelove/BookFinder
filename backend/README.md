# Server setup 

## Create a virtual environment
Use [Creating virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) as a reference. 

```
$ python -m venv path_to_environment
```

## Activate the virtual environment
```
$ source env/bin/activate
```

## Install dependencies
```
(env)$ pip install -r requirements.txt
```

## Run all database migrations
```
(env)$ python manage.py db init
(env)$ python manage.py db migrate
(env)$ python manage.py db upgrade
```

## Run the server application
```
(env)$ python runserver.py
```

Navigate to [http://localhost:5000](http://localhost:5000)
