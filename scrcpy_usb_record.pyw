import os

from pathlib import Path
from datetime import datetime

current_date = datetime.now()

new_d = 0
new_m = 0
number = 0

i = 1

date1 = [current_date.day, current_date.month, i]
date2 = [new_d, new_m, number]

for x in range(len(date1)):
    if date1[x] < 10:
        date2[x] = f"0{date1[x]}"
    else:
        date2[x] = f"{date1[x]}"

while True:
    file_path = Path(f"..\\records\\file_{str(current_date.year)[2:]}_{date2[1]}_{date2[0]}_{date2[2]}.mp4")

    if not file_path.is_file():
        os.system(f"adb kill-server")
        os.system(f"scrcpy --video-codec=h264 --video-encoder=c2.android.avc.encoder --print-fps --video-bit-rate=2M --video-buffer=50 -t -r {file_path}")
        break
    else:
        date2[2] = int(date2[2]) + 1
        if int(date2[2]) < 10:
            date2[2] = f"0{date2[2]}"