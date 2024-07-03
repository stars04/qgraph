import pandas as pd
import matplotlib.pyplot as plt

#===============================================================
#=               Step 0: Recover Data from java texts          =
#===============================================================
#For debugging
log = open("pylog.txt", "w")
log.write("The program was initialized \n \n")
#_______________________________________________________________
ncsv = 0
gname = ""
ng = 0
count = 0
kw = ["Number of CSV's : ", "Name of Graph : ", "Number of Graphs : "]
passoff = open('../python/passoff.txt', 'r', encoding='utf8')
lines = passoff.readlines()
for l in lines:
    if l.startswith(kw[0]):
        ncsv = int(l.removeprefix(kw[0]).strip())
    if l.startswith(kw[1]):
        gname = l.removeprefix(kw[1]).strip()
    if l.startswith(kw[2]):
        ng = int(l.removeprefix(kw[2]).strip())
passoff.close()
log.write("We made it past reading the files \n")
log.write("ncsv="+str(ncsv)+"\n"+"gname="+gname+"\n"+"ng="+str(ng)+"\n")
csvpaths = open('../python/csvpaths.txt', 'r', encoding='utf8')
lines = csvpaths.readlines()
path = [None]*ncsv
for l in lines:
    path[count] = l.replace("\n","")
    count += 1
csvpaths.close()
#===============================================================
#=               Step 1: Read Data and Prepare to plot         =
#===============================================================
x = [None]*ncsv
y = [None]*ncsv
csv = [None]*ncsv
labels = [None]*ncsv
for n in range(ncsv):
    csv[n] = pd.read_csv(path[n])
    x[n] = csv[n].iloc[:, 3:4]
    y[n] = csv[n].iloc[:, 4:5]
    labels[n] = "csv_" + str(n)

#Put some color codes in here
colors = ['b', 'r', 'b', 'g']
log.write("axis were assigned \n")
log.close()
#===============================================================
#=               Step 2: Plot the CSV data                     =
#===============================================================
if ng == 1:
    fig, ax = plt.subplots(figsize=(10, 10))
    if ncsv == 1:
        ax.plot(x[0], y[0], color=colors[0], linewidth=3)
    elif ncsv > 1:
        for n in range(ncsv):
            ax.plot(x[n], y[n],label=labels[n], color=colors[n], linewidth=3)
    plt.xticks(fontsize=12, weight='bold')
    plt.yticks(fontsize=12, weight='bold')
    ax.set_title(gname, fontsize=16, weight='bold', y=1.05) 
    ax.legend(loc='best', fontsize='small', fancybox=True, framealpha=0.5)
    
    plt.savefig('../plots/'+gname+".SVG", format='svg')
    plt.show()
elif ng > 1:
    for n in range(ng):
        fig, ax = plt.subplots(figsize=(10, 10))
        ax.plot(x[n], y[n],label=labels[n], color=colors[n], linewidth=3)
        plt.xticks(fontsize=12, weight='bold')
        plt.yticks(fontsize=12, weight='bold')
        ax.legend(loc='best', fontsize='small', fancybox=True, framealpha=0.5)
        plt.savefig('../plots/'+gname+str(n)+".SVG", format='svg')
        plt.close()
