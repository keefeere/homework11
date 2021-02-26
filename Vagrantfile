# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

Vagrant.configure("2") do |config|
    config.vm.define "monitoring" do |node|

      node.vm.network "private_network", ip: "192.168.50.2"
      node.vm.box = "ubuntu/focal64"
      node.vm.box_version = "20201210.0.0"
      node.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook.yml"
      end
      node.vm.disk :disk, name: "backup", size: "10GB"

      node.vm.provider "virtualbox" do |v|
        v.memory = 1024
        v.cpus = 1
      end

    end

    config.vm.define "proxy" do |node|

      node.vm.network "private_network", ip: "192.168.50.3"
      node.vm.box = "ubuntu/focal64"
      node.vm.box_version = "20201210.0.0"
      node.vm.provision "ansible" do |ansible|
        ansible.playbook = "playbook-proxy.yml"
      end

      node.vm.provider "virtualbox" do |v|
        v.memory = 1024
        v.cpus = 1
      end

    end

end


