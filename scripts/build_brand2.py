import os, numpy as np
from PIL import Image
from scipy import ndimage
from clean_alpha import clean
U='/root/.claude/uploads/f7294483-4829-5296-b611-df88e1922830/'
O='jobzee-design/project/assets/'
def fit(im, W=240, H=260, pad=6):
    im=im.crop(im.getbbox()); im.thumbnail((W-2*pad, H-2*pad), Image.LANCZOS)
    c=Image.new('RGBA',(W,H),(0,0,0,0)); c.alpha_composite(im,((W-im.width)//2, H-pad-im.height)); return c
# brand: user's own files
mark=Image.open(U+'3ab29460-image.png').convert('RGBA'); mark=mark.crop(mark.getbbox()); mark.save(O+'brand/jobzee-mark.png')
logo=Image.open(U+'145e2608-image.png').convert('RGBA'); logo=logo.crop(logo.getbbox()); logo.save(O+'brand/jobzee-logo.png')
st=Image.open(U+'7bba4703-image.png').convert('RGBA'); st=st.crop(st.getbbox()); st.save(O+'brand/jobzee-logo-stacked.png')
al=np.asarray(logo)[:,:,3].max(0); w=logo.width
start=int(w*0.12); gap=next(i for i in range(start,w) if al[i]<8)
word=logo.crop((gap,0,w,logo.height)); word=word.crop(word.getbbox()); word.save(O+'brand/jobzee-wordmark.png')
print('mark',mark.size,'logo',logo.size,'word',word.size)
# mascots from the attached poses
M={'salut':'de65bb15','trist':'9f91eadd','ups':'07f31eec','arata':'ed0dd0fe','bani':'b522770a','alearga':'be9cedca','doarme':'858a2dfb'}
for k,f in M.items():
    fit(clean(Image.open(U+f+'-image.png').convert('RGBA'))).save(O+'mascot/zee-%s.png'%k)
# illustration cards (keep their own cream background, rounded)
for k,f in (('card-bravo','8333acaa'),('card-asistent','5a2903df')):
    im=Image.open(U+f+'-image.png').convert('RGBA'); im.save(O+'mascot/zee-%s.png'%k)
# thumbs-up cut-out from the card: remove cream background connected to the border
im=Image.open(U+'8333acaa-image.png').convert('RGBA'); a=np.asarray(im).astype(np.int32)
rgb=a[...,:3]; mx=rgb.max(-1); mn=rgb.min(-1)
warm=(rgb[...,0]>235)&(rgb[...,1]>215)&(rgb[...,2]>190)&((mx-mn)<45)
lab,_=ndimage.label(warm|(a[...,3]<20))
edge=np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]]))
bg=np.isin(lab,edge[edge>0])
a[...,3][bg]=0
cut=Image.fromarray(a.astype(np.uint8),'RGBA')
fit(cut).save(O+'mascot/zee-fericit.png')
print(sorted(os.listdir(O+'mascot')))
