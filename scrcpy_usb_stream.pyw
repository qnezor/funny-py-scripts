import os
import sys

os.system(f"adb kill-server")
os.system(f"scrcpy --video-codec=h264 --video-encoder=c2.android.avc.encoder --print-fps --video-bit-rate=26M --video-buffer=50 -t")