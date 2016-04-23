import os
import numpy as np
import matplotlib.pyplot as plt
import copy

from SmileyFace import SmileyFace
from utils.image import to_gray, plot_images
from utils.io import pickle_load, pickle_save

def gen_data(num_data = 100, dir_data='/tmp', fn_data='data.pkl'):
    data = []
    
    range_x_eye_offset = [0.1, 0.2]
    range_y_eye = [0.35, 0.45]
    range_w_eye = [0.05, 0.1]
    range_h_eye = [0.05, 0.1]
    
    range_t_mouth = [0.5, 0.65]
    range_w_mouth = [0.2, 0.55]
    range_h_mouth = [0.2, 0.3]
    
    range_w_face = [0.8, 0.95]
    range_h_face = [0.8, 0.95]
    
    sf_ref = SmileyFace()
    for i in np.arange(num_data):
        sf = copy.deepcopy(sf_ref)
        sf.rand_face(range_x_eye_offset=range_x_eye_offset,
                     range_y_eye=range_y_eye,
                     range_w_eye=range_w_eye,
                     range_h_eye=range_h_eye,
                     range_t_mouth=range_t_mouth,
                     range_w_mouth=range_w_mouth,
                     range_h_mouth=range_h_mouth,
                     range_w_face=range_w_face,
                     range_h_face=range_h_face)
        A = sf.gen_img(os.path.join(dir_data, 'imgs/face%d.png' % i))

        data.append(A)
        
    
    pickle_save(data, os.path.join(dir_data, fn_data))
    

def plot_data(dir_data='/tmp', fn_data='data.pkl'):
    data = pickle_load(os.path.join(dir_data, fn_data))
    #print data[0].shape
    shape = data[0].shape[0:2]
    print shape
    data = np.array([255-to_gray(A).flatten() for A in data])
    plot_images(data, 
        10, 10, shape,
        border=2,
        reshape=True, figsize=None, colorbar=False,
        idx_highlight=None,
        vmin=0, vmax=255)
    
    plt.show()

    
def main():
    np.random.seed(1)
    dir_data = os.path.join(os.path.expanduser('~'), 'data/SmileyFace')
    fn_data = 'data.pkl'
    gen_data(dir_data=dir_data, fn_data=fn_data)
    plot_data(dir_data=dir_data, fn_data=fn_data)

if __name__ == '__main__':
    main()
    print 'finished'