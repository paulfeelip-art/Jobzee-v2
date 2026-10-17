import numpy as np, glob
from PIL import Image
from scipy import ndimage
def clean(im, thr=16):
    a=np.asarray(im.convert('RGBA')).astype(np.int32)
    rgb=a[...,:3]; al=a[...,3]
    bgc=np.array([248,246,242])
    d=np.sqrt(((rgb-bgc)**2).sum(-1))
    mx=rgb.max(-1); mn=rgb.min(-1)
    lowsat=(mx-mn)<14
    bglike=(al>0)&(d<thr)&lowsat
    # shadows: light warm greys under the feet (not part of figure) -> also bg-like when very low saturation and bright
    shadow=(al>0)&lowsat&(mx>205)&(mx<246)&(d<60)
    seed=(al<20)
    cand=bglike|shadow|seed
    lab,_=ndimage.label(cand)
    reach=np.isin(lab, np.unique(lab[seed]))
    reach&=~seed
    al2=al.copy(); al2[reach]=0
    # soften edge
    al2=ndimage.uniform_filter(al2.astype(np.float32),size=2).astype(np.int32)
    al2[al<20]=0
    out=np.dstack([rgb,al2]).astype(np.uint8)
    return Image.fromarray(out,'RGBA')
if __name__=='__main__':
    import sys
    for f in sorted(glob.glob('jobzee-design/project/assets/mascot/*.png')):
        im=Image.open(f)
        if getattr(im,'n_frames',1)>1:
            frames=[]
            for i in range(im.n_frames):
                im.seek(i); frames.append(clean(im.convert('RGBA')))
            frames[0].save(f,save_all=True,append_images=frames[1:],duration=83,loop=0,disposal=1,blend=0)
        else:
            clean(im).save(f)
        print('cleaned',f.split('/')[-1])
    # mark: remove glossy near-white highlight inside the wrench cutout
    f='jobzee-design/project/assets/brand/jobzee-mark.png'
    a=np.asarray(Image.open(f).convert('RGBA')).astype(np.int32)
    rgb=a[...,:3]; mx=rgb.max(-1); mn=rgb.min(-1)
    hl=(mx-mn<60)&(mn>170)
    a[...,3][hl]=0
    Image.fromarray(a.astype(np.uint8),'RGBA').save(f)
    f='jobzee-design/project/assets/brand/jobzee-logo.png'
    a=np.asarray(Image.open(f).convert('RGBA')).astype(np.int32)
    rgb=a[...,:3]; mx=rgb.max(-1); mn=rgb.min(-1)
    a[...,3][(mx-mn<60)&(mn>170)]=0
    Image.fromarray(a.astype(np.uint8),'RGBA').save(f)
