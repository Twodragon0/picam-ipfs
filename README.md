
## Install
Install with python3 in Raspberry Pi 3b+ or 4:
```sh
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install gpac python python3 git python-pip python3-pip python-picamera python3-picamera python-pil python3-pil python-numpy python3-numpy python-scipy python3-scipy -y
git clone https://github.com/Twodragon0/picam-ipfs.git
```
## USB Storage Setup for Data

```sh
sudo mount /dev/sda1 /media/pi/3312-22-34C
sudo nano /etc/fstab
```
Insert Info and please reboot:
/dev/sda1 /media/pi/3312-22-34C vfat gid=1000,uid=1000 0 2

Install with pip:
```sh
pip install ipfshttpclient
pip3 install ipfshttpclient
```

# Picam with python3 

"PiMotion.py" runs on the Pi, recording 30-second segments of 1080p 8 fps video as .h264 from the camera to ramdisk. For each .h264 file, it also writes a .txt file recording the amount of motion detected every 2 frames (1/4 sec).

```sh
cd picam-ipfs
chmod +x ipfs_http_client.py PiMotion.py 
python3 PiMotion.py
```

"proc.sh" and "batchjpeg.py" run together on the remote host, in the directory where the files are. They convert the raw .h264 files to .mp4 with MP4Box, and then use the 'avconv' program to extract the still frames with motion (marked out in the *.txt logfiles) and save them as jpegs.

Running of Integrate shell code (PiMotion.py, batchjpeg.py, and ipfs_http_client.py):
```sh
cd data/
./proc.sh
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

## Private ipfs Network usage in Docker

In Raspberry pi4, IPFS used to arm32v7:
```sh
docker run -d --name ipfs_host -v $ipfs_staging:/export -v $ipfs_data:/data/ipfs -p 4003:4003 -p 127.0.0.1:8082:8082 -p 127.0.0.1:5003:5003 yrzr/go-ipfs-arm32v7:latest
docker exec -it <container_id> /bin/ash
```
In docker, remove public bootstrap. Make swarm.key:
```sh
ipfs bootstrap rm all
ipfs bootstrap add /ip4/192.241.213.72/tcp/4001/p2p/Qma4bvcDe5sXZbBqiexX4Tf8zB4bpVxr7UHFnfozFiFtTv
vi /data/ipfs/swarm.key
export LIBP2P_FORCE_PNET=1 
ipfs swarm peers
```
Container Restart
```sh
docker stop <container_id>
docker start <container_id>
docker exec -it <container_id> /bin/ash
# ipfs swarm peers
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
sudo apt remove golang -y && sudo apt-get autoremove -y
sudo source ~/.profile
```
Test:
```sh
go version
```
