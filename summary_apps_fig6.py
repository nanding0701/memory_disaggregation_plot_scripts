import matplotlib.pyplot as plt
import math


font = { 'size'   : 15}
plt.rc('font', **font)
markersize = 10

colors = ['b','r','g','m','y','c']
styles = ['o','s','v','^','D',">","<","*","h","H","+","1","2","3","4","8","p","d","|","_",".",","]

fig = plt.figure(1,figsize=(10.67,6.6))
plt.clf()
ax = fig.gca()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('Memory Capacity [GB]')
ax.set_ylabel('Local:Remote Memory Ratio ')

xmin = 1
xmax = 5.1
ymin = 0.8
ymax = 5000

ax.set_xlim(10**xmin, 10**xmax)
ax.set_ylim(ymin, ymax)

xlim = ax.get_xlim()
ylim = ax.get_ylim()


ax.hlines(y=65.5, xmin=4096, xmax=1000000, linewidth=2, color='black')
plt.vlines(x=512, ymin=ymin, ymax=ymax, colors='black', lw=2)
plt.vlines(x=40, ymin=ymin, ymax=ymax, colors='black', lw=2,ls='--')
plt.vlines(x=256, ymin=ymin, ymax=ymax, colors='black', ls='--',lw=2)
plt.vlines(x=4096, ymin=ymin, ymax=ymax, colors='black',lw=2)


myx=[]
myy=[]
myupper=[]
mylower=[]
for i in range(512,4096):
    myx.append(i)
    myy.append(65.5*(4096/i))
    myupper.append(ymax)
    mylower.append(ymin)
ax.plot(myx,myy,c='k',lw=2)

zonename=['HBM bound (0 memory node)','HBM bound\n (Disaggregated)','PCIe NIC bound\n (Disaggregated)']
ax.axvspan(10**xmin, 512, alpha=0.5, color='cornflowerblue')
ax.annotate(zonename[0], (10**xmin*1.2, ymax/2),c='k',weight='bold')

ax.annotate(zonename[1], (10**4+500, 120),c='k',weight='bold')
ax.fill_between(
    myx, myy, myupper, where=(myy <= myupper),
    interpolate=True, color="yellowgreen", alpha=0.25)

ax.annotate(zonename[2], (10**4+500, 5),c='k',weight='bold')
ax.fill_between(
    myx, myy, mylower, where=(myy >= mylower),
    interpolate=True, color="moccasin", alpha=0.25)

myx=[4096,10**xmax]
myy=[65.5,65.5]
myupper=[ymax,ymax]
mylower=[ymin,ymin]
ax.fill_between(
    myx, myy, myupper, where=(myy <= myupper),
    interpolate=True, color="yellowgreen", alpha=0.25)

ax.fill_between(
    myx, myy, mylower, where=(myy >= mylower),
    interpolate=True, color="moccasin", alpha=0.25)

#ResNET, DeepCAM, CosmoFlow, DASSA, adept(traceback), adept, PASTIS, TOAST
mem=[0.15*1000,8.8*1000,5.1*1000,3.8*1000, 4.45*1000, 63,363,1000]
LR=[3993,1927,399,1000, 477, 477,435,278]
appname=['ResNET-50', 'DeepCAM', 'CosmoFlow', 'DASSA', 'ADEPT(traceback)', 'ADEPT', 'PASTIS', 'TOAST']
for i in range(0,len(mem)):
    if mem[i] < 512:
        mycolor='b'
    elif LR[i] > 65.5:
        mycolor='g'
    else:
        mycolor='orange'
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
ax.plot(ddr_gb,lr,c='darkred',lw=2)
ax.annotate(appname[0], (ddr_gb[math.floor(len(ddr_gb)/3)], lr[math.floor(len(ddr_gb)/3)]),c='darkred',weight='bold',fontsize=12)
#stream
appname=['STREAM']
lr=2
plt.axhline(y=lr, color='darkred', linestyle='-')

ax.annotate(appname[0], (ddr_gb[math.floor(len(ddr_gb)/3)], lr) ,c='darkred',weight='bold',fontsize=12)


ax.grid(b=True, which='major', color='grey', linestyle='-')
ax.grid(b=True, which='minor', color='grey', linestyle='--')
plt.savefig('summary_apps_fig6.pdf')

