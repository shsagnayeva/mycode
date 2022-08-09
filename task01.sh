#!/bin/bash

# Read input
echo "Please enter user name"
read USERNAME

echo "Please enter group name"
read GROUPNAME

# Add username
sudo adduser $USERNAME

# Add group
sudo groupadd $GROUPNAME

# Assign group to user
sudo usermod -aG $GROUPNAME $USERNAME
