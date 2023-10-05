import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from datetime import datetime, timedelta


def plot_style(theme):
    """
    define custom mpl plot style, 'dark' or 'light' theme
    """
    axis_lw=.5
    tick_size=0
        
    params_dict={'dark':{'edge_color':'.94','tick_color':'.3','face_color':(.97,.97, .96),'grid_color':'1','grid_lw':1},
                    'light':{'edge_color':'.75','tick_color':'.3','face_color':'1','grid_color':'.75','grid_lw':.4}}

    plt.rcParams['axes.facecolor'] = params_dict[theme]['face_color']
    plt.rcParams['axes.linewidth'] = axis_lw
    plt.rcParams['axes.edgecolor'] = params_dict[theme]['edge_color']
    plt.rcParams['axes.axisbelow'] = True
    plt.rcParams['axes.labelcolor'] = params_dict[theme]['tick_color']


    plt.rcParams['xtick.direction'] ='out'
    plt.rcParams['ytick.direction'] ='out'

    plt.rcParams['xtick.major.size'] = tick_size
    plt.rcParams['ytick.major.size'] = tick_size
        
    plt.rcParams['xtick.minor.size'] = tick_size
    plt.rcParams['ytick.minor.size'] = tick_size

    plt.rcParams['xtick.color'] = params_dict[theme]['tick_color']
    plt.rcParams['ytick.color'] = params_dict[theme]['tick_color']

    plt.rcParams['grid.color'] = params_dict[theme]['grid_color']
    plt.rcParams['grid.linewidth'] = params_dict[theme]['grid_lw']
    plt.rcParams['grid.linestyle'] = '-'



def format_xaxis_time(ax,t_start,t_end):
    """
    format the time xaxis
    limit to t_start, t_end (datetime objects)
    """
        
    ax.set_xticks(pd.date_range(t_start, t_end,freq='W'),minor=False)
    ax.set_xticks(pd.date_range(t_start.replace(hour=1), t_end.replace(hour=1),freq='MS'),minor=True)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('\n%b'))
    
    ax.set_xlim(t_start - timedelta(days=0), t_end + timedelta(days=1))
    
    for tl in ax.xaxis.get_majorticklabels():
        tl.set_horizontalalignment("left")
    for tl in ax.xaxis.get_minorticklabels():
        tl.set_horizontalalignment("left")
            
    ax.tick_params(labelsize=9, length=0)
    ax.grid(True)  #,which='x')