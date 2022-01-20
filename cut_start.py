#argv[1] = video file name (xxxvid.mp4)
#argv[2] = start timestamp in seconds (eg. 00, 05)

import subprocess, sys

subprocess.run('ffmpeg -ss 00:00:'+sys.argv[2]+' -i "'+sys.argv[1]+'" -c copy "cs_'+sys.argv[1]+'"', shell=True)