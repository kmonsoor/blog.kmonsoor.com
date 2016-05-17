---
Title: Ubuntu - Change your Update Server to Fastest Mirror
Date: 2016-05-17
Tags:  ubuntu, mirror, apt-get, update, upgrade, fastest, server 
Slug:  change-ubuntu-update-server-to-fastest-mirror
Summary:  Each of our decisions make or break the path for the next opportunity or disaster. Be it for our worldly life or the life-after.
Version: 0.1.0
Status: Draft
---

## Prelude
By default, Ubuntu sets the update server pointing to its own. It is the safest bet for Ubuntu. But not for users. Hence, Ubuntu also provides a list of mirror sites which help Ubuntu to alleviate the load from all over the world.


## On GUI

> It works on geolocation, giving me the local server, which is waaaayy slower where I am. The network temporal distance is the important factor here, not spatial distance (http://askubuntu.com/a/9035/113604)


## whats's for Command-line

    git clone https://github.com/jblakeman/apt-select.git
    cd apt-select
    ./apt-select.py -c -t 3 -m one-week-behind

Choose one with the lowest ping time. Then,
    sudo mv /etc/apt/sources.list /etc/apt/sources.list.backup && sudo mv sources.list /etc/apt/

Then, recommended that you run:

    sudo apt-get update
    
Then, if you want:
    
    sudo apt-get upgrade
    
    
