#!/bin/bash
# Maintenance script: update system and restart Apache

set -e

if [ -f /etc/os-release ] && grep -q "Amazon Linux" /etc/os-release; then
  dnf -y update || yum -y update
  systemctl restart httpd
else
  apt update -y
  apt upgrade -y
  systemctl restart apache2
fi
