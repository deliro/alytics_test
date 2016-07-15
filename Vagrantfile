# -*- mode: ruby -*-

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 5555, host: 5555
  config.vm.synced_folder ".", "/home/vagrant/project"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y postgresql
    apt-get install -y libpq-dev
    apt-get install -y python-virtualenv
    apt-get install -y python3-dev
    apt-get install -y rabbitmq-server
    rabbitmq-plugins enable rabbitmq_management
    service rabbitmq-server restart
    rabbitmqctl add_user myuser mypassword
    rabbitmqctl add_vhost myvhost
    rabbitmqctl set_user_tags myuser mytag
    rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
  SHELL
end
