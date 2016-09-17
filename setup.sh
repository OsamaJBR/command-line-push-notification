#!/bin/bash
# Maintainer jbr.osama@gmail.com

DOWNLOAD_LINK=https://codeload.github.com/OsamaJBR/push-notifier/zip/master
CONFIG_PATH=/etc/notifier.conf
BIN_FILE=/usr/local/bin/notifier
TEMP=/tmp

if [ "$(id -u)" != "0" ]; then
    echo "You have to run this script as root"
    exit 2
fi

PKG_MANAGER=$( command -v yum || command -v apt-get ) || { echo "Neither yum nor apt-get found"; exit 2;}
command -v wget &>> /dev/null || $PKG_MANAGER install -y wget
command -v unzip &>> /dev/null || $PKG_MANAGER install -y unzip

wget $DOWNLOAD_LINK -O $TEMP/push-notifier.zip
cd $TEMP && unzip $TEMP/push-notifier.zip
cp $TEMP/push-notifier-master/notifier.conf $CONFIG_PATH
cp $TEMP/push-notifier-master/notifier.py $BIN_FILE
chmod +x $BIN_FILE

echo "### INSTALLING PYTHON REQUIREMENTS ###"
$PKG_MANAGER install -y python-requests python-argparse python-configparser

read -p "Have you installed SimplePush app on your android ? If yes, please insert it now or press enter : " AUTH_KEY
if [ -z $AUTH_KEY];then
    echo "Installation is done, please add the SimplePush key in $CONFIG_PATH"
else
    sed -i "s/YOUR_KEY/$AUTH_KEY/" $CONFIG_PATH
    echo "Installation and configuration are done."
    echo "Sending a test notification" && $BIN_FILE -t 'Test' -m 'Sent to test the installation'
fi