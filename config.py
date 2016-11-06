try:
    from configparser import ConfigParser
except:
    from ConfigParser import ConfigParser


config = ConfigParser()
config.read("config.ini")

HOST = config.get("SERVER", "HOST")
PORT = int(config.get("SERVER", "PORT"))
DEBUG = config.get("SERVER", "DEBUG").lower() in ["true", "yes"]

DATABASE_FILE_NAME = config.get("DATABASE", "NAME")
