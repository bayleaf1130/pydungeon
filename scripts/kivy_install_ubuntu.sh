#!/bin/sh

sudo apt-get install python-setuptools python-pygame python-opengl \
  python-enchant python-dev build-essential python-pip libgl1-mesa-dev \
  libgles2-mesa-dev zlib1g-dev

python3 -m pip install --upgrade Cython==0.29.10
python3 -m pip install pygments docutils pillow
python3 -m pip install kivy
