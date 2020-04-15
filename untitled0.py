# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 02:28:58 2019

@author: sudhe
"""

img=255*imread(r"C:/Datasets/try.png")
img=img.astype(np.uint8)

img=img[:,:,0]

img=img.flatten()

binary=list(map(bin,img))

bin_strings=list(map(lambda x:x[2:].zfill(8),binary))

img2=list(map(lambda y:list(map(lambda x:int(x),y)),bin_strings))

image=list()

for i in img2:
    image.extend(i)

image=np.asarray(image)
image=image.reshape(len(image)//int(math.log2(m)),int(math.log2(m)))    
mqam_op=list(map(lambda y: int(y,2),list(map(lambda x:''.join(list(map(str,x))),list(image)))))