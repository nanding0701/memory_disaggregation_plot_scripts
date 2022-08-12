import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw,shrink=0.5)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom",size=15)
    cbar.ax.tick_params(labelsize=14)

    num_elements = len(farmers)
    X_Tick_List = []
    for item in range (0,num_elements):
        X_Tick_List.append(item)
    ax.set_xticks(ticks=X_Tick_List)
    ax.set_xticklabels(col_labels)
    num_elements = len(vegetables)
    X_Tick_List = []
    for item in range (0,num_elements):
        X_Tick_List.append(item)
    ax.set_yticks(ticks=X_Tick_List)
    ax.set_yticklabels(row_labels)
    # Show all ticks and label them with the respective list entries.
    #ax.set_xticks(np.arange(data.shape[1]), labels=col_labels,size=20)
    #ax.set_yticks(np.arange(data.shape[0]), labels=row_labels,size=20)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False,labelsize=16)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor",size=16)

    ## Turn spines off and create white grid.
    #ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

vegetables = ["100%", "80%", "60%", "50%",
              "40%", "20%","10%","1%",]
farmers = ["10K:0.1K","10K:0.5K","10K:1K", "10K:2.5K",
           "10K:5K", "10K:10K", "10K:20K"]


mem_capacity=np.array([
    [0.04,	0.20,	0.41,			1.02,		2.05,	4.10,	8.19],
    [0.05,	0.26,	0.51,			1.28,		2.56,	5.12,	10.24],
    [0.07,	0.34,	0.68,			1.71,		3.41,	6.83,	13.65],
    [0.08,	0.41,	0.82,			2.05,		4.10,	8.19,	16.38],
    [0.10,	0.51,	1.02,			2.56,		5.12,	10.24,	20.48],
    [0.20,	1.02,	2.05,			5.12,		10.24,	20.48,	40.96],
    [0.41,	2.05,	4.10,			10.24,		20.48,	40.96,	81.92],
    [4.10,	20.48,	40.96,			102.40,		204.80,	409.60,	819.20]
])

mem_bw=np.array([
    [1.00,	5.00,	10.00,			25.00,		50.00,	100.00,	100.00],
    [1.25,	6.25,	12.50,			31.25,		62.50,	100.00,	100.00],
    [1.67,	8.33,	16.67,			41.67,		83.33,	100.00,	100.00],
    [2.00,	10.00,	20.00,			50.00,		100.00,	100.00,	100.00],
    [2.50,	12.50,	25.00,			62.50,		100.00,	100.00,	100.00],
    [5.00,	25.00,	50.00,			100.00,		100.00,	100.00,	100.00],
    [10.00,	50.00,	100.00,			100.00,		100.00,	100.00,	100.00],
    [100.00,100.00,	100.00,			100.00,		100.00,	100.00,	100.00]
])



fig, ax = plt.subplots(1,2,figsize=(15,10))
im, cbar = heatmap(mem_capacity, vegetables, farmers, ax=ax[0],
                   cmap="magma_r", cbarlabel="Available remote memory capacity\n per compute node [GB]")
texts = annotate_heatmap(im, valfmt="{x:.2f}",size=12,fontweight="bold")

im, cbar = heatmap(mem_bw, vegetables, farmers, ax=ax[1],
                   cmap="magma_r", cbarlabel="Available remote bandwidth [GB/sec]")
texts = annotate_heatmap(im, valfmt="{x:.0f}",size=12,fontweight="bold")

fig.tight_layout()
plt.savefig('system_design_space.pdf')

