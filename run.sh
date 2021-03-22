#!/bin/bash -x
sudo ansible-playbook deploy.yml -i host --key-file ~/.ssh/tobkey -vvv