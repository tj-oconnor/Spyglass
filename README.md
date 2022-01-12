# "SpyGlass" Mitmproxy scripts

This repository contains the scripts used in our paper, "Through the Spyglass: Towards IoT Companion App Man-in-the-Middle Attacks" [[bib]](paper/cset2021oconnor.bib) [[pdf]](paper/cset2021oconnor.pdf)

## Installation

These scripts rely on mitmrpoxy. See <https://docs.mitmproxy.org/stable/overview-installation/> for installing mitmproxy. 

## Usage

Start a script with the (-s) option for either *mitmproxy* or *mitmweb*

```
mitmweb -s <script.py>
```

## Example impacts of lack of SSL-Pinning

hiding users on the devices:
- [august-hide-user.py](code/august-hide-user.py) 
- [sifely-hide-admins.py](code/sifely-hide-admins.py)
- [utec-hide-user.py](code/utec-hide-user.py)

clearing logs on the devices:
- [simplisafe-logs-clear.py](code/simplisafe-logs-clear.py)
- [lockly-logs-clear.py](code/lockly-logs-clear.py)
- [smartthigns-logs-clear.py](code/smartthigns-logs-clear.py)

revealing sensitive information:
- [alexa-speaking-spy.py](code/alexa-speaking-spy.py)
- [nightowl-reveal-backdoor.py](code/nightowl-reveal-backdoor.py)
- [blink-creds.py](code/blink-creds.py)

manipulating integrity of images:
- [roku-image-spoof.py](code/roku-image-spoof.py)
- [google-home-spoof.py](code/google-home-spoof.py)
- [momentum-camera-spoof.py](code/momentum-camera-spoof.py)
- [nest-camera-spoof.py](code/nest-camera-spoof.py)
- [wyze-camera-spoof.py](code/wyze-camera-spoof.py)

controlling state of devices:
- [schlage-force-unlock.py](code/schlage-force-unlock.py)
- [hue-force-off.py](code/hue-force-off.py)  


