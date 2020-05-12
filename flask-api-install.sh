#!/usr/bin/env bash
# https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux?view=powershell-7#centos-7
set -e

yum install -y sudo  # Always use sudo for escalations
curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo || true
sudo yum install -y powershell

# pwsh

python3 -m venv venv
# source venv/bin/activate
# pip3 install -r requirements.txt
# ./flask-api.py
