import subprocess, glob, os, math, json

type = ".mp4"

mp4_vids = glob.glob("*"+type)

for vid in mp4_vids:
    size = (os.path.getsize(vid)) * 9.31 / (math.pow(10, 10)) #size in GB
    print(size)
    if size >= 2:
        result = subprocess.check_output(f'ffprobe -v quiet -show_streams -select_streams v:0 -of json "{vid}"',shell=True).decode()
        duration_min = float(json.loads(result)['streams'][0]['duration'])/60
        p = math.ceil(size/1.99)
        duration_pp = math.ceil(duration_min/p)
        subprocess.run('ffmpeg -i "'+vid+'" -c copy -map 0 -segment_time 00:'+str(duration_pp)+':00 -f segment -reset_timestamps 1 '+vid+'%03d.mp4', shell=True)
        
# ffmpeg -ss 00:01:00 -to 00:02:00  -i input.mp4 -c copy output.mp4
#ffmpeg -loop 1 -i image.jpg -i Bryan\ Adams\ -\ Heaven.mp3 -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest output.mp4