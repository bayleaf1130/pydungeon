#!/bin/sh

# You can use homebrew and install all the dependencies like this
if command -v brew &> /dev/null ; then
    sudo brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer
    echo "Installing cython and kivy..."
    pip3 install Cython==0.29.10
    pip3 install kivy
elif command -v port &> /dev/null ; then
    sudo port -N install libsdl2 libsdl2_image libsdl2_ttf libsdl2_mixer
    echo "You need to install gstreamer manually or the next commands will not work, the compiler will fail!!!"
    echo "Installing cython and kivy..."
    pip3 install Cython==0.29.10
    pip3 install kivy
else
    echo "Install either Macports or homebrew for your OSX system"
fi

