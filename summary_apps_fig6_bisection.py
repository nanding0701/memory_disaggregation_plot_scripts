import matplotlib.pyplot as plt
import math
import numpy as np


font = { 'size'   : 15}
plt.rc('font', **font)
markersize = 10

colors = ['r','maroon','m','indigo','orangered']
styles = ['o','s','v','^','D',">","<","*","h","H","+","1","2","3","4","8","p","d","|","_",".",","]

fig = plt.figure(1,figsize=(12,8))
plt.clf()
ax = fig.gca()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Memory Capacity [GB]')
ax.set_ylabel('Local:Remote Memory Ratio ')

xmin = 1
xmax = 6.1
ymin = 0.8
ymax = 10000

ax.set_xlim(10**xmin, 10**xmax)
ax.set_ylim(ymin, ymax)

xlim = ax.get_xlim()
ylim = ax.get_ylim()


plt.vlines(x=512, ymin=ymin, ymax=ymax, colors='black', lw=2)
plt.vlines(x=40, ymin=ymin, ymax=ymax, colors='black', lw=2,ls='--')
plt.vlines(x=256, ymin=ymin, ymax=ymax, colors='black', ls='--',lw=2)
#plt.vlines(x=1024, ymin=ymin, ymax=ymax, colors='black',lw=2)
plt.vlines(x=4096, ymin=ymin, ymax=ymax, colors='black',lw=2)


myx=[]
myxinter=[]
myy=[]
myupper=[]
mylower=[]
myyintra=[]
myyinter=[]
myupperinter=[]
mylowerinter=[]


for i in range(512,4096):
    myx.append(i)
    myy.append(65.5*(4096/i))
    myupper.append(ymax)
    mylower.append(ymin)
    myupperinter.append(728)

ax.plot(myx,myy,c='k',lw=2)
ax.hlines(y=65.5, xmin=4096, xmax=10**xmax, linewidth=2, color='black')
ax.hlines(y=131, xmin=2048, xmax=10**xmax, linewidth=2, color='black')
ax.hlines(y=728, xmin=512, xmax=10**xmax, linewidth=2, color='black')


zonename=['Only Local Memory Access','Disaggregation\nNo Performance Penalty','Disaggregation\n Injection Bandwidth Bound','Disaggregation\n Bisection Bandwidth Bound']
ax.axvspan(10**xmin, 512, alpha=0.5, color='cornflowerblue')
ax.annotate(zonename[0], (10**xmin*1.05, 2000),c='k',weight='bold')
ax.annotate(zonename[1], (1000000,4000),c='k',weight='bold',ha='right')
ax.annotate(zonename[2], (1000000, 15),c='k',weight='bold',ha='right')
ax.annotate(zonename[3], (1000000,300),c='k',weight='bold',ha='right')

ax.fill_between(
    myx, myy, mylower, where=(np.array(myy) >= np.array(mylower)),
    interpolate=True, color="sandybrown", alpha=0.25)

ax.fill_between(
    myx, myy, myupperinter, where=(np.array(myy) <= np.array(myupperinter)),
    interpolate=True, color="darkgrey", alpha=0.25)


myx=[512,10**xmax]
myy=[728,728]
myupper=[ymax,ymax]
mylower=[ymin,ymin]
ax.fill_between(
    myx, myy, myupper, where=(np.array(myy) <= np.array(myupper)),
    interpolate=True, color="yellowgreen", alpha=0.25)

myx=[4096,10**xmax]
myy=[65.5,65.5]
myupper=[728,728]
ax.fill_between(
    myx, myy, mylower, where=(np.array(myy) >= np.array(mylower)),
    interpolate=True, color="sandybrown", alpha=0.25)

ax.fill_between(
    myx, myy, myupper, where=(np.array(myy) <= np.array(myupper)),
    interpolate=True, color="darkgrey", alpha=0.25)

##ResNET, adept, PASTIS, DeepCAM, CosmoFlow, DASSA, adept(traceback),  TOAST
mem=[0.15*1000,63,363,8.8*1000,5.1*1000,3.8*1000, 4.45*1000,1000]
LR=[3993,477,435,1927,399,1000, 477,278]
appname=['ResNET-50', 'ADEPT', 'PASTIS','DeepCAM', 'CosmoFlow', 'DASSA', 'ADEPT(traceback)',  'TOAST']
#for i in range(0,3):
for i in range(0,len(mem)):
    if i < 3:
        mycolor='b'
    else:
        mycolor=colors[i-3]
    plt.scatter(mem[i], LR[i],  c=mycolor, s=50)
    plt.annotate(appname[i], (mem[i], LR[i]),c=mycolor,weight='bold',fontsize=12)


#EXTENSION
mem=[4506.93, 3949.155, 2896.155, 1213.515]
LR=[314,633,1555,3402]
kmer=['kmer=21','kmer=33','kmer=55','kmer=77']
plt.plot(mem, LR,  c='g', marker='s',lw=2)
for i in range(0,len(mem)):
    plt.annotate(kmer[i], (mem[i], LR[i]),c='g',weight='bold',fontsize=12)


#gemm
appname=['GEMM']
ddr_gb=[1024,	2048,	4096,	8192,	16384,	32768,	65536,	131072,	262144,	524288,	1048576,	2097152]
lr=[48,	68,	92,	81,	80,	81,	83,	84,	86,	87,	87,	88]
ax.plot(ddr_gb,lr,c='darkred',marker='s',lw=2)
ax.annotate(appname[0], (ddr_gb[math.floor(len(ddr_gb)/100)], lr[0]-10),c='darkred',weight='bold',fontsize=12)

#stream
appname=['STREAM']
lr=2
plt.axhline(y=lr, color='darkred', linestyle='-')
ax.annotate(appname[0], (ddr_gb[math.floor(len(ddr_gb)/3)], lr*0.75) ,c='darkred',weight='bold',fontsize=12)

#superlu
appname=['SuperLU 1-1','SuperLU 50-1','SuperLU 100-1']
lr=[4,101,201]
ddr=[10240,10240,10240]
plt.plot(ddr, lr,  c='deeppink', marker='s',lw=2)
for i in range(0,len(lr)):
    ax.annotate(appname[i], (10240, lr[i]*1.1) ,c='deeppink',weight='bold',fontsize=12)

#Eigensolver
appname=['Eigensolver']
lr=[3.3,3.3,3.3]
ddr=[1024,4096, 16384]
plt.plot(ddr, lr,  c='darkmagenta', marker='s',lw=2)
ax.annotate(appname[0], (1024, 3.3*0.75) ,c='darkmagenta',weight='bold',fontsize=12)

ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.savefig('summary_apps_fig6_bisection.pdf')

