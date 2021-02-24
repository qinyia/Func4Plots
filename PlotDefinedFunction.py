import matplotlib as mpl
from matplotlib import ticker
from mpl_toolkits.axes_grid1 import make_axes_locatable

# ==========================================================================================================================
def make_colorbar(ax, units, fh, mappable, **kwargs):
    '''
    Nov 23, 2020: a function to add colorbar fitted well with the figure
    Referred from: https://github.com/pydata/xarray/issues/619
    units: the unit of colorbar
    fh: fontsize of colorbar label font size
    '''
    divider = make_axes_locatable(ax)
    orientation = kwargs.pop('orientation', 'vertical')
    if orientation == 'vertical':
        loc = 'right'
    elif orientation == 'horizontal':
        loc = 'bottom'
        
    cax = divider.append_axes(loc, '5%', pad='5%', axes_class=mpl.pyplot.Axes)
    cb = ax.get_figure().colorbar(mappable, cax=cax, orientation=orientation,extend='both')
    cb.set_label(units,fontsize=fh)
    cb.ax.tick_params(labelsize=fh)
    tick_locator = ticker.MaxNLocator(nbins=9)
    cb.locator = tick_locator
    cb.update_ticks()

# ==========================================================================================================================

def add_common_colorbar(fig,im,axes,units,orientation='vertical',nbins=9,fontsize=15):
    '''
    Feb 12, 2021: generate a common colorbar for several specific subplots.
    For example, subplots on the same row or the same column.
    -----------------------
    Inputs:
    fig -- 
    im -- return handle. 
    axes --- the list for all subplots.
    units --- unit of colorbar.
    orientation --- direction of colorbar.
    nbins --- number of labeled ticks. default: 9
    fontsize --- label fontsize for colorbar. 
    '''
    pos1 = axes[-1].get_position() # get the original position for the last subplot 
    if orientation == 'vertical':
        pos2 = [pos1.x0 + pos1.width + 0.01, pos1.y0,  pos1.width / 20.0, pos1.height ]   
    else:
        pos2 = [pos1.x0, pos1.y0 - 0.01, pos1.width, pos1.height / 25.0]
        
    cbar_ax = fig.add_axes(pos2)
    cb = fig.colorbar(im,ax=axes, orientation=orientation, cax=cbar_ax)
    cb.set_label(units,fontsize=fontsize)
    cb.ax.tick_params(labelsize=fontsize)
    tick_locator = ticker.MaxNLocator(nbins=nbins)
    cb.locator = tick_locator
    cb.update_ticks()
    
# ==========================================================================================================================

def create_nested_dict_ND(n, type):
    '''
    Jan 27, 2021:
    create a nested dictionary with number of dimensions and type.
    inputs:
    n -- number of dimension for new dictionary
    type -- type of each element, like float, str
    '''
    from collections import defaultdict
    if n == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: create_nested_dict_ND(n-1, type))

# ==========================================================================================================================

def create_nested_dict():
    ''' 
    Jan 27, 2021:
    create a nested dictionary with no limit on dimensions and type.
    ref: https://stackoverflow.com/questions/5369723/multi-level-defaultdict-with-variable-depth/8702435#8702435
    '''
    from collections import defaultdict
    return defaultdict(lambda: create_nested_dict())
