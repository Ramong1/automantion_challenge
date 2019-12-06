#!/usr/bin/env bash

# Install requirements for pyenv

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

# Install pyenv

curl https://pyenv.run | bash

# setup pyenv environment in .bash_profile

echo '' >> ~/.bash_profile
echo 'export PATH="/home/vagrant/.pyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

. ~/.bash_profile

# Install the latest version of python or which ever version you want.

pyenv install 3.8.0
pyenv global 3.8.0

echo "Done installing pyenv."
echo "Rebooting"

# Assumes you setup vagrant user with sudo access in your vagrant box build.
sudo reboot
