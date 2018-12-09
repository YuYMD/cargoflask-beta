import os
from datetime import timedelta

SECRET_KEY = 'insecurekeyfordev'

DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = 'postgresql://snakeeyes%40cargoflowdb:devpassword01!@cargoflowdb.postgres.database.azure.com:5432/snakeeyes'
SQLALCHEMY_TRACK_MODIFICATIONS = False

REMEMBER_COOKIE_DURATION = timedelta(days=90)
