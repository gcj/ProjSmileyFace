import numpy as np
import cairo

def init_img(w):
    A = np.zeros((w, w, 4), dtype=np.uint8)
    surface = cairo.ImageSurface.create_for_data(
        A, cairo.FORMAT_ARGB32, w, w)
    ctx = cairo.Context(surface)
    ctx.scale(w/1.0, w/1.0)
    
    # default with white background
    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.paint()

    return A, ctx, surface
    
   
def draw_ellipse(ctx, x_ctr, y_ctr, width, height, angle=0, line_width=0.1, fill=False, rgb_color=(0,0,0)):
    ctx.set_line_width(line_width)
    r,g,b = rgb_color
    ctx.set_source_rgb(r, g, b)
 
    ctx.save()
    ctx.translate(x_ctr, y_ctr)
    ctx.rotate(angle)
    ctx.scale(width / 2.0, height / 2.0)
    ctx.arc(0.0, 0.0, 1.0, 0.0, 2.0 * np.pi)
    ctx.restore()
    
    if fill == True:
        ctx.stroke()
        ctx.fill()
    else:
        ctx.stroke()
    
def draw_spline(ctx, line_width=0.1, fill=False, rgb_color=(0,0,0), **kwargs):
    """
    kwargs: x1,y1,x2,y2,x3,y3
    """
    ctx.set_line_width(line_width)
    r,g,b = rgb_color
    ctx.set_source_rgb(r, g, b)

    ctx.move_to(kwargs['x0'], kwargs['y0'])
    ctx.curve_to(kwargs['x1'], kwargs['y1'],
                 kwargs['x2'], kwargs['y2'],
                 kwargs['x3'], kwargs['y3'])
    
    ctx.stroke()
    
