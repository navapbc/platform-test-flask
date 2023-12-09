"""
Configuration file for the Gunicorn server used to run the application in production environments.

Attributes:
    bind(str): The socket to bind. Formatted as '0.0.0.0:$PORT'.
    workers(int): The number of worker processes for handling requests.
    threads(int): The number of threads per worker for handling requests.

For more information, see https://docs.gunicorn.org/en/stable/configure.html
"""

import os

from src.app_config import AppConfig

app_config = AppConfig()

bind = app_config.host + ":" + str(app_config.port)
# Calculates the number of usable cores and doubles it. Recommended number of workers when running in a
# container is 2 (see https://pythonspeed.com/articles/gunicorn-in-docker/)
workers = 2
threads = 4

# Use gevent worker class which is most appropriate for web apps which may make block network requests
# (like database queries for example). Under the hood, this approach monkeypatches blocking I/O calls
# with compatible cooperative counterparts from gevent package that allow the worker to switch threads.
# Read more in the following resources:
# https://docs.gunicorn.org/en/latest/design.html,
# https://medium.com/@danieldng/use-gevent-when-your-gunicorn-worker-is-waiting-for-data-180efef96367,
# https://stackoverflow.com/questions/69372896/gunicorn-with-gevent-performance-gain
worker_class = "gevent"
