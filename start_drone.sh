#!/bin/bash
echo "图传接收中..."
gst-launch-1.0 udpsrc port=5600 ! application/x-rtp ! rtph264depay ! avdec_h264 ! autovideosink