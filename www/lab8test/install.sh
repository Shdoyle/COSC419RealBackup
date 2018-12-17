#!/bin/bash
clear

echo -e "\n***Installing Python-pip***"
sudo yum -y install python-pip
echo -e "***Finished python-pip install***\n"

echo -e "\n***Upgrading Python-pip***"
sudo  pip install --upgrade pip
echo -e "***Finished Python-pip Install***\n"

echo -e "\n***Installing Flask***"
sudo yum -y install flask
echo -e "***Finished Flask install***\n"

echo -e "\n***Installing Repo for Passenger***"
sudo curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo
echo -e "***Finished Repo for Passenger install***\n"

echo -e "\n***Installing Passenger***"
sudo yum install -y mod_passenger || sudo yum-config-manager --enable cr && sudo yum install -y mod_passenger
echo -e "***Finished Passenger install***\n"

echo -e "\n***Restarting Server***"
sudo service httpd restart
echo -e "***Finished Server Restart***\n"

echo -e "\n***Creating Directory For Flask***"
sudo mkdir /var/www/lab8test
ls /var/www -l
echo -e "***Finished Creating Directory For Flask***\n"

echo -e "\n***Copying Files to Flask Directory***"
sudo cp -f -R -v * /var/www/lab8test
echo -e "***Finished Copying Files to Flask Directory***\n"

echo -e "\n***Copying  myapp.conf to /etc/httpd/conf.d/lab8test.conf***"
sudo cp /etc/httpd/conf.d/myapp.conf /etc/httpd/conf.d/lab8test.conf
ls /etc/httpd/conf.d -l
echo -e "***Finished Copying Files to Flask Directory***\n"

echo -e "\n***Restarting Server***"
sudo service httpd restart
echo -e "***Finished Server Restart***\n"

########################################
#Test Code to Undue the Folder copying##
########################################
#echo -e "\n***Deleting***"
#chmod -R 777 /var/www/lab8test/*
#chmod 777 /etc/httpd/conf.d/lab8test.conf
#rm -R -d /var/www/lab8test
#rm /etc/httpd/conf.d/lab8test.conf
#ls /etc/httpd/conf.d -l
#ls /var/www/ -l
#echo -e "***Finished Deleting***\n"
########################################






