#!/usr/bin/env python3
import subprocess, datetime, sys

log = open("/var/log/daily-backup.log", "a")
sys.stdout = sys.stderr = log

print(f"=== daily-backup.py started: {datetime.datetime.utcnow()} ===")

INSTANCE_ID = "i-0d99354b8d40491c6"
DATE = datetime.date.today().isoformat()
AMI_NAME = f"webserver-backup-{DATE}"

print(f"Using INSTANCE_ID={INSTANCE_ID}")
print(f"Creating AMI: {AMI_NAME}")

subprocess.run(
    f'aws ec2 create-image '
    f'--instance-id {INSTANCE_ID} '
    f'--name {AMI_NAME} '
    f'--no-reboot '
    f'--tag-specifications "ResourceType=image,Tags=[{{Key=Project,Value=WebServer}},{{Key=Backup,Value=Daily}}]"',
    shell=True,
    check=True
)

print("AMI create-image request sent.")
print(f"=== daily-backup.py finished: {datetime.datetime.utcnow()} ===")
