---
layout: post
title: Setting up a Raspberry Pi 4
tags: raspberrypi mac linux
---

I decided to start playing with the Raspberry Pi, and this post is here to summarize the steps I went through to set it up.

# Setting up the OS

Some packages come equipped with a micro SD card already burned with an image.
I thought it would be more interesting to do that setp myself.
It's actually pretty simple as all you need to do, besides buying a SD card, is install [etcher](https://www.balena.io/etcher/), then follow the steps:
* you can point etcher directly to the URL of the image you are trying to burn. In this case, I used [Raspberry Pi OS with desktop and recommended software](https://www.raspberrypi.org/software/operating-systems/).
* select the location of your micro SD card.

I actually first re-formatted the micro SD card to the FAT format using Disk Utility. But I'm not even sure this was needed as etcher might very well take care of that step.


