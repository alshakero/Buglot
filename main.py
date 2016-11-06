
from api import webApp
from config import HOST, PORT, DEBUG


if __name__ == "__main__":
    print(" * HOST: %s, PORT: %d, DEBUG: %s" % (HOST, PORT, DEBUG))
    webApp.run(host=HOST, port=PORT, debug=DEBUG)
