
## Install
Install with python3 in Raspberry Pi 3b+ or 4:
```sh
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install gpac python3 git python3-pip python3-picamera python3-pil python3-numpy python3-scipy -y
git clone https://github.com/Twodragon0/picam-ipfs.git
```
Install with pip:

```sh
pip3 install ipfshttpclient
```

# Picam with python3 

"PiMotion.py" runs on the Pi, recording 30-second segments of 1080p 8 fps video as .h264 from the camera to ramdisk. For each .h264 file, it also writes a .txt file recording the amount of motion detected every 2 frames (1/4 sec).

```sh
cd picam-ipfs
python3 PiMotion.py
```

"proc.sh" and "batchjpeg.py" run together on the remote host, in the directory where the files are. They convert the raw .h264 files to .mp4 with MP4Box, and then use the 'avconv' program to extract the still frames with motion (marked out in the *.txt logfiles) and save them as jpegs.

```sh
cd data/
sh proc.sh
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
