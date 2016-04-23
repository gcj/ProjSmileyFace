import numpy as np
import matplotlib.pyplot as plt

def to_gray(A):
    A_gray = (A[:,:,0]*2220.0 + A[:,:,1]*7076.0 + A[:,:,2]*713.0) / 10000.0
    A_gray = A_gray.astype(np.uint8)
    return A_gray



def plot_images(X, 
        n_rows, n_cols, img_shape,
        border=2,
        reshape=True, figsize=None, colorbar=False,
        idx_highlight=None,
        vmin=None, vmax=None): 
    """
    row-major
    if there are 12 imgs and the layout is 3x4, then
    012
    345
    678
    9AB
    """
    
    if idx_highlight == None:
        idx_highlight_set = set([])
    else:
        idx_highlight_set = set(idx_highlight)
    
    if figsize == None:
        figsize = (n_cols, n_rows)
        
    h = plt.figure(figsize=figsize)
    ax = plt.gca()
    img_width, img_height = img_shape

    n_imgs =  n_rows * n_cols
    n_imgs = min(n_imgs, X.shape[0])
    A = np.zeros( (n_rows*(img_height+border)+border, n_cols*(img_width+border)+border) ) + 0.5
    for i in range(n_imgs):
        i_row = img_height * (i/n_cols) + (i/n_cols+1)*border
        j_row = i_row + img_height

        i_col = img_width * (i%n_cols) + (i%n_cols+1)*border
        j_col = i_col + img_width

        A[i_row:j_row,i_col:j_col] = np.reshape(X[i], img_shape)

        if i in idx_highlight_set:
            ax.add_patch(Rectangle((i_col-0.5, i_row-0.5), width=img_width, height=img_height, edgecolor='r', fill=False, linewidth=3))

            


    plt.imshow(A, interpolation='nearest', vmin=vmin, vmax=vmax)
    plt.axis('off')
    plt.set_cmap('binary')
    if colorbar == True:
        plt.colorbar()
        
    return h