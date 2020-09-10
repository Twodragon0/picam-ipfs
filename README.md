
## Install
Install with python3 in Raspberry Pi 3b+ or 4:
```sh
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install gpac python python3 git python-pip python3-pip python-picamera python3-picamera python-pil python3-pil python-numpy python3-numpy python-scipy python3-scipy -y
git clone https://github.com/Twodragon0/picam-ipfs.git
```
## USB Storage Setup for Data
Insert UUID Info and please reboot:

```sh
sudo mount /dev/sda1 /media/pi/3312-22*
sudo nano /etc/fstab
UUID=dde9*       /kist   vfat    defaults,auto,_netdev   0       0
```

Install with pip for py-ipfs(ipfs v.0.5.X, v.0.4.X):
```sh
sudo pip install ipfshttpclient
sudo pip3 install ipfshttpclient
```

Migrating from ipfs-http-client 0.4.x to 0.6.0:
```sh
git clone https://github.com/ipfs/py-ipfs-http-client.git
cd py-ipfs-http-client
pip3 install flit
flit install --pth-file
```


## SD card capacity expansion after installing Raspberry Pi

```sh
sudo raspi-config
```
Advanced Options -> A1 Expand Filesystem, And then Reboot 

# Picam with python3 

"PiMotion.py" runs on the Pi, recording 30-second segments of 1080p 8 fps video as .h264 from the camera to ramdisk. For each .h264 file, it also writes a .txt file recording the amount of motion detected every 2 frames (1/4 sec).

```sh
cd picam-ipfs
sudo chmod 777 ipfs_http_client.py PiMotion.py 
python3 PiMotion.py
```

"proc.sh" and "batchjpeg.py" run together on the remote host, in the directory where the files are. They convert the raw .h264 files to .mp4 with MP4Box, and then use the 'avconv' program to extract the still frames with motion (marked out in the *.txt logfiles) and save them as jpegs.

Running of Integrate shell code (PiMotion.py, batchjpeg.py, and ipfs_http_client.py):
```sh
cd data/
sudo ./proc.sh
```

MP4Box is easily installed by 'sudo apt-get install gpac' on any Debian-based system. Note I had to compile avconv from the current github source, because the standard apt-get version does not do frame-accurate seeking, which is needed for this application. 

Reference:
https://github.com/jbeale1/PiCam1


## Connect PiCam-IPFS using python3

Convert txt file to IPFS (working)

1. Upload video file to ipfs gateway using Python3
2. Can get video data in IPFS Network
3. All Raspberry Pi video can show form IPFS Network URL

```sh
ipfs daemon &
python3 ipfs_http_client.py
```

Result: IPFS hash
Qm <hash> 

## Error solution = TabError: inconsistent use of tabs and spaces in indentation
When code shows Tab or 4 spaces error, autopep8 of pip3 has to install. and it uses Filename.py.
```sh
pip3 install --upgrade autopep8
autopep8 -i stest2.py 
```
W: Problem unlinking the file /var/lib/apt/lists/partial/a* - PrepareFiles (30: Read-only file system)
```sh
sudo mount -o remount,rw /
```

## Install Golang 1.14:
```sh
wget https://dl.google.com/go/go1.14.3.linux-armv6l.tar.gz
sudo tar -C /usr/local -xzf go1.14.3.linux-armv6l.tar.gz
sudo rm go1.14.3.linux-armv6l.tar.gz
sudo nano ~/.profile
export PATH=$PATH:/usr/local/go/bin # put into ~/.profile
```
If already installed old golang with apt-get, please remove this:
```
sudo apt remove golang && sudo apt-get autoremove -y
sudo source ~/.profile
```
Test:
```sh
go version
```
