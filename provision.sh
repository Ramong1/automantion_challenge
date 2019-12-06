#!/usr/bin/env bash

# Install any needed items as root.
# Here we can bootstrap the system with things such as ntpd, salt-minion, etc...

HOSTNAME=ubuntu1
IP=10.1.10.254

apt-get update -y
apt-get upgrade -y

echo 'Done.'
