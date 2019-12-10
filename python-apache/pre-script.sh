#!/bin/bash

# install apache
sudo apt update
sudo apt install apache2

# install mod_wsgi for python
sudo apt-get install libapache2-mod-wsgi-py3 python-dev

pip3 install -r requirements.txt
