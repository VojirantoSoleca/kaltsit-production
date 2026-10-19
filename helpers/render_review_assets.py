"""Supplement bundled pet previews with exact-atlas loops and labeled stills."""
from pathlib import Path
import argparse, json, subprocess, sys
from PIL import Image, ImageDraw

p = argparse.ArgumentParser()
p.add_argument('--atlas', required=True)
p.add_argument('--output', required=True)
p.add_argument('--ffmpeg')
a = p.parse_args()
out = Path(a.output); out.mkdir(parents=True, exist_ok=True)
atlas = Image.open(a.atlas).convert('RGBA')
states = ['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']
counts = [6,8,8,4,5,8,6,6,6]
timings = [[280,110,110,140,140,320],[120]*7+[220],[120]*7+[220],[140]*3+[280],[140]*4+[280],[140]*7+[240],[150]*5+[260],[120]*5+[220],[150]*5+[280]]
def cell(r,c):
    return atlas.crop((192*c,208*r,192*(c+1),208*(r+1)))
def panel(im, title):
    imout=Image.new('RGB',(240,256),(239,242,234))
    imout.paste(im,(24,32),im)
    ImageDraw.Draw(imout).text((12,10),title,fill=(39,52,40))
    return imout
def gif(frames,durations,path):
    frames[0].save(path,save_all=True,append_images=frames[1:],duration=durations,loop=0,disposal=2,optimize=False)
frames=[]; durations=[]
for r,(name,n) in enumerate(zip(states,counts)):
    folder=out/'encoded-frames'/name; folder.mkdir(parents=True,exist_ok=True)
    for c in range(n):
        im=cell(r,c); im.save(folder/f'{c:02}.png')
        frames.append(panel(im,f'{name} | {c+1}/{n}')); durations.append(timings[r][c])
gif(frames,durations,out/'all-states.gif')
seq=[(0,c) for c in range(6)]+[(4,c) for c in range(5)]+[(0,c) for c in range(6)]
gif([cell(r,c) for r,c in seq],timings[0]+timings[4]+timings[0],out/'idle-jump-idle.gif')
labels=['000','022.5','045','067.5','090','112.5','135','157.5','180','202.5','225','247.5','270','292.5','315','337.5']
if atlas.height==2288:
    gif([panel(cell(9+i//8,i%8),f'look {label} deg') for i,label in enumerate(labels)],[150]*16,out/'look-loop.gif')
still=Image.new('RGB',(960,256),(239,242,234))
for i,(r,c) in enumerate([(0,0),(3,2),(4,2),(5,4)]):
    still.paste(panel(cell(r,c),f'{states[r]} | frame {c+1}'),(240*i,0))
still.save(out/'four-state-stills.png')
if a.ffmpeg:
    mp4=out/'all-states.mp4'
    proc=subprocess.Popen([a.ffmpeg,'-y','-f','rawvideo','-pix_fmt','rgb24','-s','240x256','-r','100','-i','-','-an','-c:v','libx264','-pix_fmt','yuv420p','-movflags','+faststart',str(mp4)],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    for im,ms in zip(frames,durations):
        for _ in range(max(1,round(ms/10))): proc.stdin.write(im.tobytes())
    proc.stdin.close(); proc.stdin=None
    stdout,stderr=proc.communicate()
    if proc.returncode: raise RuntimeError(stderr.decode(errors='replace'))
print(json.dumps({'ok':True,'atlas':str(Path(a.atlas).resolve()),'output':str(out.resolve()),'mp4':bool(a.ffmpeg)},indent=2))
