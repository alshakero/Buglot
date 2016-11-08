# @Author: Fadi Hanna Al-Kass (ceo@shaykeapp.com)

import rethinkdb as rdb
from api import run
from config import configs


if __name__ == "__main__":
    # Establish connection with the database engine
#    rdb.connect(configs["RETHINKDB"]["HOST"], configs["RETHINKDB"]["PORT"]).repl()

    # Create the required database and tables


    # Run the server
    run\
    (
        host = configs["SERVER"]["HOST"],
        port = configs["SERVER"]["PORT"],
        debug = configs["SERVER"]["DEBUG"],
        rdb = rdb
    )
