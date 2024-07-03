import matplotlib.pyplot as plt
import pandas as pd

#===============================================================
#=               Step 0: Recover Data from java texts          =
#===============================================================







#===============================================================
#=               Step 1: Plot the CSV data                     =
#===============================================================
if ugn == 1:
    fig, ax = plt.subplots(figsize=(10, 10))
    if ng == 1:
        ax.plot(x[0], y[0], color ="b", linewidth=3)
    elif ng > 1:
        for x in ng:
            ax.plot(x[x], y[x],label=labels[x], color="b", linewidth=3)
    plt.xticks(fontsize=12, weight='bold')
    plt.yticks(fontsize=12, weight='bold')
    
    ax.legend(loc='best', fontsize='small', fancybox=True, framealpha=0.5)
    
    plt.savefig('../plots/'+gname+".SVG", format='svg')
    plt.show()
elif ugn > 1:
    for x in ugn:
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x[x], y[x],label=labels[x], color=colors[x], linewidth=3)
    plt.xticks(fontsize=12, weight='bold')
    plt.yticks(fontsize=12, weight='bold')
    ax.legend(loc='best', fontsize='small', fancybox=True, framealpha=0.5)
    plt.savefig('../plots/'+gname+x+".SVG", format='svg')
    plt.close()
