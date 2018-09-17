import sys
import json
import matplotlib
#matplotlib.use('Agg') # for systems without X11
import matplotlib.pyplot as pyplot

def main():
    with open("best.fit.json", 'r') as inf:
        intensity_dict = json.load(inf)

    set_plot_options()

    x = sorted(intensity_dict.keys(), key=lambda x: int(x))
    y = sorted(intensity_dict.keys(), key=lambda x: int(x))
    intensity = [[intensity_dict[i][j] for i in x] for j in y]

    pyplot.imshow(intensity, cmap="inferno", aspect='auto', origin='lower')
    pyplot.colorbar()

    pyplot.xlabel("Packet Model Index")
    pyplot.xticks(range(15))
    pyplot.ylabel("Packet Model Index")

    pyplot.savefig("best.fit.pdf")
    pyplot.close()

def set_plot_options():
    options = {
        #'backend': 'PDF',
        'font.size': 14,
        'figure.figsize': (4,3),
        'figure.dpi': 100.0,
        'figure.subplot.left': 0.12,
        'figure.subplot.right': 1.0,
        'figure.subplot.bottom': 0.15,
        'figure.subplot.top': 0.95,
        'grid.color': '0.1',
        'grid.linestyle': ':',
        #'grid.linewidth': 0.5,
        'axes.grid' : False,
        'axes.grid.axis' : 'y',
        #'axes.axisbelow': True,
        'axes.titlesize' : 'x-small',
        'axes.labelsize' : 'small',
        'axes.formatter.limits': (-3,3),
        'xtick.labelsize' : 10,
        'ytick.labelsize' : 10,
        'lines.linewidth' : 2.0,
        'lines.markeredgewidth' : 0.5,
        'lines.markersize' : 8,
        'legend.fontsize' : 9,
        'legend.fancybox' : False,
        'legend.shadow' : False,
        'legend.borderaxespad' : 0.5,
        'legend.numpoints' : 1,
        'legend.handletextpad' : 0.5,
        'legend.handlelength' : 1.6,
        'legend.labelspacing' : .75,
        'legend.markerscale' : 1.0,
        # turn on the following to embedd fonts; requires latex
        'ps.useafm' : True,
        'pdf.use14corefonts' : True,
        'text.usetex' : True,
    }

    for option_key in options:
        matplotlib.rcParams[option_key] = options[option_key]

    if 'figure.max_num_figures' in matplotlib.rcParams:
        matplotlib.rcParams['figure.max_num_figures'] = 50
    if 'figure.max_open_warning' in matplotlib.rcParams:
        matplotlib.rcParams['figure.max_open_warning'] = 50
    if 'legend.ncol' in matplotlib.rcParams:
        matplotlib.rcParams['legend.ncol'] = 50

if __name__ == '__main__': sys.exit(main())
