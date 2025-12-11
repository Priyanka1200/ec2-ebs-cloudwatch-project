#!/usr/bin/env python3
import subprocess, sys, os

def run(cmd): subprocess.check_call(cmd, shell=True)

is_amazon = os.path.isfile("/etc/os-release") and "Amazon Linux" in open("/etc/os-release").read()

if is_amazon:
    run("dnf -y update || yum -y update")
    run("systemctl restart httpd")
else:
    run("apt update -y && apt upgrade -y")
    run("systemctl restart apache2")
