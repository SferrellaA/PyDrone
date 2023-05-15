# PyDrone
Python-based drone c2 reverse engineering

## Libraries used
http://kiminewt.github.io/pyshark/
~~https://pypi.org/project/pyrcrack/~~ pyrcrack is not developed to the point I need

## Setup
airodump requires firmware and a wifi chipset that supports monitor mode
The linkysys usb wifi dongle I initially tried does not have the correct chipset
Rasbian's default firmware also no longer supports monitor mode on it's onboard wifi chip
A canakit one worked though
Apparently kali comes with drivers that support more kinds of dongles?

CLI commands:
```
iwconfig # to see available devices
sudo iwconfig wlan1 mode monitor
sudo airodump-ng wlan1
```