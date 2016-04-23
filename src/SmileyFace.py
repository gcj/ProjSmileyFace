from utils.io import pickle_load, pickle_save
from utils.cairo_ext import *

class SmileyFace(object):
    def __init__(self,
                 dim_img = 32,
                 x_ctr_face = 0.5,
                 y_ctr_face = 0.5,
                 w_face = 0.8,
                 h_face = 0.8,
                 x_eye_offset = 0.15,
                 y_eye = 0.4,
                 w_eye = 0.05,
                 h_eye = 0.1,
                 w_mouth = 0.4,
                 t_mouth = 0.6,
                 h_mouth = 0.2):
        self.dim_img = dim_img
        self.x_ctr_face = x_ctr_face
        self.y_ctr_face = y_ctr_face
        self.w_face = w_face
        self.h_face = h_face
        
        self.x_eye_offset = x_eye_offset
        self.y_eye = y_eye
        self.w_eye = w_eye
        self.h_eye = h_eye
        
        self.w_mouth = w_mouth
        self.t_mouth = t_mouth
        self.h_mouth = h_mouth
        
        self.ctx = None
        self.surface = None
        self.A = None

    def init_img(self):
        self.A, self.ctx, self.surface = init_img(self.dim_img)

    def gen_img(self, fn=None):
        self.init_img()
        self.draw_face()
        self.draw_eye()
        self.draw_mouth()
        
        if fn is not None:
            self.surface.write_to_png(fn)
            
        return self.A
        
    def draw_face(self):
        draw_ellipse(self.ctx, 
                     x_ctr=self.x_ctr_face, y_ctr=self.y_ctr_face,
                     width=self.w_face, height = self.h_face,
                     line_width=0.04)

    def draw_eye(self):
        draw_ellipse(self.ctx, 
                     x_ctr=self.x_ctr_face - self.x_eye_offset, y_ctr=self.y_eye, 
                     width=self.w_eye, height=self.h_eye, fill=True)
        draw_ellipse(self.ctx, 
                     x_ctr=self.x_ctr_face + self.x_eye_offset, y_ctr=self.y_eye, 
                     width=self.w_eye, height=self.h_eye, fill=True)

    def draw_mouth(self):
        l_mouth = self.x_ctr_face - 0.5*self.w_mouth
        r_mouth = self.x_ctr_face + 0.5*self.w_mouth
        b_mouth = self.t_mouth + self.h_mouth
        t_mouth = self.t_mouth
        
        draw_spline(self.ctx,
                    x0 = l_mouth, y0 = t_mouth,
                    x1 = l_mouth, y1 = b_mouth,
                    x2 = r_mouth, y2 = b_mouth,
                    x3 = r_mouth, y3 = t_mouth)
  
    
    def rand_face(self, range_x_eye_offset=None,
                     range_y_eye=None,
                     range_w_eye=None,
                     range_h_eye=None,
                     range_t_mouth=None,
                     range_w_mouth=None,
                     range_h_mouth=None,
                     range_w_face=None,
                     range_h_face=None):
        if range_w_face is not None:
            self.w_face = np.random.uniform(*range_w_face)
            
        if range_h_face is not None:
            self.h_face = np.random.uniform(*range_h_face)
        
        if range_x_eye_offset is not None:
            self.x_eye_offset = np.random.uniform(*range_x_eye_offset)
        
        if range_y_eye is not None:
            self.y_eye = np.random.uniform(*range_y_eye)
            
        if range_w_eye is not None:
            self.w_eye = np.random.uniform(*range_w_eye)
            
        if range_h_eye is not None:
            self.h_eye = np.random.uniform(*range_h_eye)

        if range_t_mouth is not None:
            self.t_mouth = np.random.uniform(*range_t_mouth)

        if range_w_mouth is not None:
            self.w_mouth = np.random.uniform(*range_w_mouth)

        if range_h_mouth is not None:
            h_max0 = self.y_ctr_face + self.h_face*0.5 - self.t_mouth - 0.05
            h_min, h_max = range_h_mouth
            if h_min > h_max0:
                range_h_mouth = [h_max0, h_max0]
            elif h_max > h_max0:
                range_h_mouth = [h_min, h_max0]
                
            self.h_mouth = np.random.uniform(*range_h_mouth)
           
  
def main():
    import matplotlib.pyplot as plt
    sf = SmileyFace()
    A = sf.gen_img('face1.png')
    #A_gray = (A[:,:,0]*2220 + A[:,:,1]*7076 + A[:,:,2]*713) / 10000.0
    A_gray = (A[:,:,0]*2220.0 + A[:,:,1]*7076.0 + A[:,:,2]*713.0) / 10000.0
    A_gray = A_gray.astype(np.uint8)
    
    print A.shape
    print A_gray
    print A_gray.dtype
    print A_gray.shape
    plt.figure()
    plt.imshow(A, interpolation="nearest")
    
    plt.figure()
    plt.imshow(A_gray, interpolation="nearest", cmap=plt.get_cmap('gray'), vmin = 0, vmax = 255)
    plt.show()
    
    
if __name__ == '__main__':
    main()
    print 'finished'
