
# Install RethinkDB
. /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | tee /etc/apt/sources.list.d/rethinkdb.list
wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
apt-get update -y
apt-get install -y rethinkdb

# Run the RethinkDB server
rethinkdb &

# Install Python package manager
apt-get install -y python-pip
