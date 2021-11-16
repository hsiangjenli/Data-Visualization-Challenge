import urllib
import json
import pandas as pd

import datetime

import cv2
from IPython.display import display, Image
import matplotlib.pyplot as plt

import geopandas as gpd

def plot(data, plot_type, column, cmap, file_name):
    h = 100
    w = 100
    if plot_type == 'normal':
        data.plot(figsize=(w,h),cmap = cmap )
    elif plot_type == 'heatmap':
        data.plot(figsize=(w,h),column = column, cmap = cmap)

    plt.savefig(f"./Images/Plot_{file_name}.png", bbox_inches='tight')
    return f"./Images/Plot_{file_name}.png"


def crop(file_name):
    image = cv2.imread(file_name)
    
    #裁切範圍
    crop_image = image[300:3000, 1300:4000, :]
    
    cv2.imshow("Cropped", crop_image)
    cv2.imwrite(file_name,crop_image)
    cv2.destroyAllWindows()

    display(Image(filename=file_name))

def get_covid19_data():
    
    url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.json'

    with urllib.request.urlopen(url) as jsonfile:
        data = json.loads(jsonfile.read().decode())

    df = pd.DataFrame(data)
    df['確定病例數'] = df['確定病例數'].apply(lambda x:int(x))
    df['個案研判日'] = [datetime.datetime.strptime(d, "%Y/%m/%d") for d in df['個案研判日']]
    
    return df


class Shape:
    def County():
        C_shp = gpd.read_file(r'./Data/County/COUNTY_MOI_1090820.shp')
        C_shp.set_index('COUNTYNAME', inplace = True)
        return C_shp
    def Town():
        t_shp = gpd.read_file(r'./Data/Town/TOWN_MOI_1100415.shp')
        t_shp.set_index('TOWNNAME', inplace = True)
        return t_shp

class Data:
    def __init__():
        
