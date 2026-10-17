# Builds brand + mascot PNGs for the canvas from the official Jobzee asset pack.
import os, glob
from PIL import Image, ImageFilter, ImageChops
import numpy as np
PK='assets/png/Jobzee_Official_Style_Asset_Pack/'
OUT='jobzee-design/project/assets/'
os.makedirs(OUT+'brand',exist_ok=True); os.makedirs(OUT+'mascot',exist_ok=True)
ref=Image.open(PK+'00_REFERENCE/SOURCE_REFERENCE_DO_NOT_MODIFY.png').convert('RGB')
S=1536/1400
def cut(box):
    return ref.crop(tuple(int(v*S) for v in box))
def key_out(img, thr=18, soft=22):
    # remove near-background light pixels: distance from local bg colour sampled at the corners
    a=np.asarray(img).astype(np.float32)
    corners=np.array([a[2,2],a[2,-3],a[-3,2],a[-3,-3]]).mean(0)
    d=np.sqrt(((a-corners)**2).sum(-1))
    alpha=np.clip((d-thr)/soft,0,1)
    # keep white gloves/shoes: they are near-white too, so protect pixels connected to the figure is hard; use saturation+brightness rule
    out=np.dstack([a, alpha*255]).astype(np.uint8)
    im=Image.fromarray(out,'RGBA')
    bbox=im.getbbox(); return im.crop(bbox) if bbox else im
def fit(im, W=240, H=260, pad=6):
    im=im.copy(); im.thumbnail((W-2*pad, H-2*pad), Image.LANCZOS)
    c=Image.new('RGBA',(W,H),(0,0,0,0)); c.alpha_composite(im,((W-im.width)//2, H-pad-im.height)); return c
# --- logo (mark + wordmark) and mark only
logo=key_out(cut((420,100,800,220)),thr=14,soft=26)
logo.save(OUT+'brand/jobzee-logo.png')
w=logo.width
# mark = left part up to first big gap in alpha columns
al=np.asarray(logo)[:,:,3].max(0)
gap=next(i for i in range(int(w*0.15),w) if al[i]<10)
mark=logo.crop((0,0,gap,logo.height)); mark=mark.crop(mark.getbbox())
sq=max(mark.size); m=Image.new('RGBA',(sq,sq),(0,0,0,0)); m.alpha_composite(mark,((sq-mark.width)//2,(sq-mark.height)//2)); m=m.resize((256,256),Image.LANCZOS); m.save(OUT+'brand/jobzee-mark.png')
word=logo.crop((gap,0,w,logo.height)); word=word.crop(word.getbbox()); word.save(OUT+'brand/jobzee-wordmark.png')
for n in ('orange','light','dark'):
    Image.open(PK+'02_APP_ICONS/mascot_app_icon_%s_512.png'%n).resize((256,256),Image.LANCZOS).save(OUT+'brand/app-icon-%s.png'%n)
print('logo',logo.size,'mark split at',gap)
# --- mascot poses (pack crops are used where clean; broken ones are re-cut from the reference)
P={ 'salut': Image.open(PK+'01_MASCOT_TRANSPARENT/jobzee_hero_waving.png'),
    'ups': Image.open(PK+'01_MASCOT_TRANSPARENT/jobzee_holding_phone.png'),
    'trist': Image.open(PK+'01_MASCOT_TRANSPARENT/jobzee_explaining.png'),
    'doarme': Image.open(PK+'01_MASCOT_TRANSPARENT/jobzee_using_laptop.png'),
    'sarbatoare': Image.open(PK+'01_MASCOT_TRANSPARENT/jobzee_jumping.png'),
    'bani': Image.open(PK+'01_MASCOT_TRANSPARENT/jobzee_running_briefcase.png'),
    'arata': Image.open(PK+'01_MASCOT_TRANSPARENT/jobzee_pointing.png'),
    'alearga': Image.open(PK+'01_MASCOT_TRANSPARENT/jobzee_running.png'),
    'fericit': key_out(cut((195,385,315,545)),thr=12,soft=20),
}
for k,im in P.items():
    im=im.convert('RGBA'); im=im.crop(im.getbbox()); fit(im).save(OUT+'mascot/zee-%s.png'%k)
# --- animated states (APNG, 12 fps) from the pack's 12-frame sequences
for state,name in (('thinking','gandeste'),('searching','cauta'),('matching','potrivire'),('listening','asculta'),('success','succes')):
    fr=[Image.open(PK+'07_ANIMATION_FRAMES/%s_%02d.png'%(state,i)).convert('RGBA') for i in range(12)]
    bb=None
    for f in fr:
        b=f.getbbox(); bb=b if bb is None else (min(bb[0],b[0]),min(bb[1],b[1]),max(bb[2],b[2]),max(bb[3],b[3]))
    fr=[fit(f.crop(bb)) for f in fr]
    fr[0].save(OUT+'mascot/zee-%s.png'%name, save_all=True, append_images=fr[1:], duration=83, loop=0, disposal=1, blend=0)
print(sorted(os.listdir(OUT+'mascot')))
