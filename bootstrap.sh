#!/usr/bin/env bash

repo_url='https://github.com/apache/cloudstack.git'
branch='4.4-forward'

echo "==== Step1: Repo Package Update and install few libs ===="
sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

echo "==== Step3: Install Python Dev Packages ===="
sudo apt-get install -y python-setuptools
sudo apt-get install -y autoconf g++ python2.7-dev
sudo apt-get install -y python-pip build-essential 

#sudo apt-get install python-dev

echo "==== Step4: Install Java 7 ==== "
sudo apt-get install -y python-software-properties
sudo add-apt-repository -y ppa:webupd8team/java
sudo apt-get update
echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
sudo apt-get install -y oracle-java7-installer
sudo apt-get install -y oracle-java7-set-default


echo "==== Step5 : Install Maven ==== "
sudo apt-get install -y maven

echo "==== Step6 : Install and Start MySql Server ==== "
echo  "mysql-server mysql-server/root_password password root" | sudo debconf-set-selections
echo  "mysql-server mysql-server/root_password_again password root" | sudo debconf-set-selections
sudo apt-get install -qq -y mysql-server
#reset password of root
mysqladmin -u root -proot password ''
service mysql start


echo "==== Step7 : Install Git ===="
sudo apt-get install -y git

echo "==== Step8: Download CS Code and Install CloudStack ===="
sudo mkdir -p /automation/cloudstack
sudo python /vagrant/buildAndDeploySimulator.py -u $repo_url -b $branch 
