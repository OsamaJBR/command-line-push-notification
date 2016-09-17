# push-notifier
Notifier is a simple script that could be added to a Linux system and give it the ability to push notifications to Android phones using SimplePush.io

### Usage : 
#### Basic
``` 
notifier -t 'Test Notifier' -m 'Notification Text Body'
``` 
![alt tag](https://i.imgflip.com/1arn0r.gif) 
#### Conditional
```
$ command_or_script && notifier -t title_title -m "success message"

$ command_or_script || notifier -t title_title -m "failure message"

$ command_or_script && notifier -t title_title -m "success message" || notifier -t command_name -m "failure message"
```

## Installation
## Android
#### MUST : Install SimplePush Application (https://simplepush.io/)
##### Copy the and add it to /etc/notifier.conf or pass it to the automatic installer.

#### Manual 
```
$ git clone git@github.com:OsamaJBR/push-notifier.git push-notifier
$ cp push-notifier/notifier.conf /etc/notifier.conf
$ sed -i 's/XXXX/YOUR_KEY/' /etc/notifier.conf  #(chage YOUR_KEY to the key you've got from simple push app)
$ cp push-notifier/notifier.py /usr/local/bin/notifier
$ chmod +x /usr/local/bin/notifier
```
#### Automated
```
sudo bash <(curl -s https://raw.githubusercontent.com/OsamaJBR/push-notifier/master/setup.sh )
```

