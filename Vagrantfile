# -*- mode: ruby -*-
# vi: set ft=ruby :

# Items that can change according to your environment:
# Update these items to match your environment before running vagrant up

# Vagrant box: I create my own custom vagrant boxes referenced here as ubuntu-s1
#    config.vm.box = "ubuntu-s1"

# Hostname: for example, ubuntu1
#    ubuntu1.vm.hostname = "ubuntu1"

# Private Key: Create your own ssh keys and add them into the private_key_path referenced here as insecure_private_key
#    config.ssh.private_key_path = ['~/.vagrant.d/insecure_private_key']

# Bridge: I bridge my adapter "p3p1" and assign it a static IP from my pool.
#    config.vm.network "public_network", :bridge => "p3p1", :ip => "10.1.10.254"


# provision.sh adds any updates you may want to run as root.
# pyenv.sh installs pyenv as the vagrant user along with the latest version of python.



##### Begin Vagrantfile #####

Vagrant.configure("2") do |config|
  config.vm.box = "ramong/ubuntu-s1"
  config.vm.define "ubuntu1" do |ubuntu1|
  config.ssh.private_key_path = ['~/.vagrant.d/insecure_private_key']
  config.ssh.insert_key = true
  config.vm.synced_folder '.', '/vagrant', disabled: true
  config.vm.network "public_network", :bridge => "p3p1", :ip => "10.1.10.254"
  ubuntu1.vm.hostname = "ubuntu1"

  # Configures provisioner.
  config.vm.provision :shell, :path => "provision.sh"

  # Configures provisioner as non-privileged user.
  config.vm.provision :shell, privileged: false, :path => "pyenv.sh"

  end

end
