# -*- mode: ruby -*-
# vi: set ft=ruby :

# @Author: Fadi Hanna Al-Kass (ceo@shaykeapp.com)


# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  # Vagrant Box Preference
  config.vm.box = "ubuntu/trusty64"

  # This is a get-around the Ubuntu tty issue
  config.vm.provision "fix-no-tty", type: "shell" do |s|
    s.privileged = false
    s.inline = "sudo sed -i '/tty/!s/mesg n/tty -s \\&\\& mesg n/' /root/.profile"
  end

  # Network Configuration
  config.vm.network "private_network", type: "dhcp"
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # Specific Development Environment Configuration
  # NOTE: If you so choose to alter the provisioning process, don't add your commands here directly. Instead,
  # modify Scripts/setup.sh to fit your preferences and needs.
  #config.vm.provision "shell", inline: "cd /vagrant/Scripts && chmod +x debug.setup.sh && sudo ./debug.setup.sh"
end
