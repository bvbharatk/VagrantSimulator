Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise32"
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.provision :shell, :path => "bootstrap.sh"
end
