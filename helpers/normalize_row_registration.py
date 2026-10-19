"""Uniform per-row scale and baseline alignment of bundled extracted pixels.

This performs only scale/translation, preserves all frame order and per-row
vertical displacement, and does not create or redraw character pixels.
"""
import argparse, json, shutil, statistics
from pathlib import Path
from PIL import Image

p=argparse.ArgumentParser()
p.add_argument('--frames-root',required=True)
p.add_argument('--output',required=True)
p.add_argument('--body-height',type=float,default=165)
p.add_argument('--baseline',type=int,default=198)
a=p.parse_args()
src=Path(a.frames_root); dst=Path(a.output); dst.mkdir(parents=True,exist_ok=True)
manifest=json.loads((src/'frames-manifest.json').read_text(encoding='utf-8'))
report=[]
for row in manifest['rows']:
    name=row['state']; paths=sorted((src/name).glob('*.png'))
    ims=[Image.open(f).convert('RGBA') for f in paths]
    bounds=[im.getchannel('A').point(lambda x:255 if x>16 else 0).getbbox() for im in ims]
    if any(b is None for b in bounds): raise ValueError(f'Empty {name} frame')
    median_h=statistics.median(b[3]-b[1] for b in bounds)
    source_ground=max(b[3] for b in bounds) if name=='jumping' else statistics.median(b[3] for b in bounds)
    scale=a.body_height/median_h
    # Preserve headroom and every generated vertical displacement.
    highest=min(b[1] for b in bounds)
    scale=min(scale,(a.baseline-6)/max(1,source_ground-highest))
    wide=max(b[2]-b[0] for b in bounds)
    scale=min(scale,180/max(1,wide))
    (dst/name).mkdir(parents=True,exist_ok=True)
    outputs=[]
    for i,im in enumerate(ims):
        sized=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
        canvas=Image.new('RGBA',(192,208))
        x=round(96-96*scale); y=round(a.baseline-source_ground*scale)
        canvas.alpha_composite(sized,(x,y))
        f=dst/name/f'{i:02}.png';canvas.save(f);outputs.append(str(f.resolve()))
    row['frames']=outputs
    row['registration']={'uniform_scale':scale,'source_ground':source_ground,'baseline':a.baseline}
    report.append({'state':name,**row['registration']})
(dst/'frames-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(dst/'row-registration.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'ok':True,'rows':report},indent=2))
