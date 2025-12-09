#!/bin/bash
# Simple daily AMI backup script (hardcoded instance-id)

LOGFILE=/var/log/daily-backup.log
exec >>"$LOGFILE" 2>&1

echo "=== daily-backup.sh started: $(date -u) ==="

INSTANCE_ID="i-0d99354b8d40491c6"

DATE=$(date +%F)
AMI_NAME="webserver-backup-$DATE"

echo "Using INSTANCE_ID=$INSTANCE_ID"
echo "Creating AMI: $AMI_NAME"

aws ec2 create-image \
  --instance-id "$INSTANCE_ID" \
  --name "$AMI_NAME" \
  --no-reboot \
  --tag-specifications "ResourceType=image,Tags=[{Key=Project,Value=WebServer},{Key=Backup,Value=Daily}]"

echo "AMI create-image request sent."
echo "=== daily-backup.sh finished: $(date -u) ==="
