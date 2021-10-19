import numpy as np
import png
import pydicom
import json
import base64
import os
import db
import requests
from sender import Req
from remove import remove
from pydicom.pixel_data_handlers.util import apply_voi_lut
import time

def getInfo(ds, path):

    data = db.payload(ds)
    try:
        textPathOne = createPng(ds, path)
        data.append(textPathOne)
        info = Req.req(data)
        if info:
            remove(path)
            remove(textPathOne)
            remove(f'{path.strip(".dcm")}.png')
            return True
        return textPathOne
    except Exception as e:
        return False

def createPng(ds, path):
    windowed = apply_voi_lut(ds.pixel_array, ds)
    
    try:

        shape = ds.pixel_array.shape
        image_2d = windowed.astype(float)
        
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 225
        image_2d_scaled = np.uint8(image_2d_scaled)

        pngPath = f'{path.strip(".dcm")}.png'

        with open(pngPath, 'wb') as png_file:
            w = png.Writer(shape[1], shape[0])
            w.write(png_file, image_2d_scaled)

        with open(pngPath, "rb") as img_file:
            my_string = base64.b64encode(img_file.read())

        textPath = f'{pngPath.strip(".png")}.txt'
        with open(textPath, 'wb') as out:
            out.write(my_string)
        return textPath
            
    except Exception as e:
        print(e)
        return True