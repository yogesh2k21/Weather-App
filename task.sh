#!/bin/bash

sudo snap install docker

#git clone https://github.com/yogesh2k21/Weather-App

#cd Weather-App

#display current directory path
echo $(pwd)

#docker-compose.yml run command
sudo docker-compose -f docker-compose.yml up -d
