#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import ffmpeg
from pprint import pprint
# read the media file from the command line
media_file = sys.argv[1]
# extract metadata from the media file
f = sys.argv[2]
with open(f,'w') as fout:
    pprint(ffmpeg.probe(media_file)["streams"], stream=fout)

