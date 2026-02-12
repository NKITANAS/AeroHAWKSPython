# AeroHAWKS 2026 Payload Code, Written in Python
Code for the HVA AeroHAWKs NASA Student Launch 2025-2026 Payload Experiment.
## Payload Functions
This payload code runs on a raspberry Pi 4, Equipped with a LoRa HAT to transmit data.
This Payload can:
* Transmit Data to a ground station via LoRa
* Extend it's soil probes and measure ground moisture data upon landing
* Detect different stages of flight with an accelerometer
## How to run
On a Raspberry Pi:
1. If python cannot be updated to a version higher than 3.14 via apt, build it from source.
2. Install [poetry](https://python-poetry.org/)
3. Run  the following commands to clone the repo:  
```bash
git clone https://github.com/NKITANAS/AeroHAWKSPython
cd AeroHAWKSPython
```
4. If built python 3.14 or higher from source:
```bash
# You may need to replace 3.14 with something else depending on how you built python
poetry env set python3.14
```
5. Install dependencies and run the project:
```bash
poetry env activate
poetry install
poetry run python src/main.py
```
6. NOTE: If any of the dependencies fail to install, or the project dosent work, make sure to check whether the corresponding system packages are installed.

## License
This code is Licesnsed under the GNU General Public License v3.