#!/usr/bin/python3
from logging import FileHandler

from flask import Flask
import settings
import logging
from flask.logging import default_handler


app = Flask(__name__, )
app.config.from_object(settings.Dev)

app.logger.removeHandler(default_handler)
app.logger.setLevel(logging.INFO)

fmt = logging.Formatter(fmt='%(asctime)s %(name)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

file_handler = FileHandler('edu.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(fmt)

app.logger.addHandler(file_handler)

