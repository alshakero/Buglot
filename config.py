# @Author: Fadi Hanna Al-Kass (ceo@shaykeapp.com)

try:
    from configparser import ConfigParser
except:
    from ConfigParser import ConfigParser


config = ConfigParser()
config.read("config.ini")

configs = {}
configs["SERVER"] = {}
configs["SERVER"]["HOST"] = config.get("SERVER", "HOST")
configs["SERVER"]["PORT"] = int(config.get("SERVER", "PORT"))
configs["SERVER"]["DEBUG"] = config.get("SERVER", "DEBUG").upper() in ("TRUE", "YES")

configs["RETHINKDB"] = {}
configs["RETHINKDB"]["HOST"] = config.get("RETHINKDB", "HOST")
configs["RETHINKDB"]["PORT"] = int(config.get("RETHINKDB", "PORT"))
configs["RETHINKDB"]["DATABASE_NAME"] = config.get("RETHINKDB", "DATABASE_NAME")
configs["RETHINKDB"]["TABLE_NAME"] = config.get("RETHINKDB", "TABLE_NAME")
