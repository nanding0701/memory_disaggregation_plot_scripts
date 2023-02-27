import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import matplotlib.patches as mpatches
font = { 'size'   : 15}
plt.rc('font', **font)

scalingFactorForRoofs = 1

smemroofs = [100, 50,28,9]
smem_roof_name = ['Bisection bandwidth=injection bandwidth\n' ,'50% Bisection bandwidth','28% Bisection bandwidth','9% Bisection bandwidth']

scomp_roof_name = ['HBM3']
scomproofs = [6552]
markersize = 10

colors = ['brown','magenta','b','g','y','c']
styles = ['o','s','v','^','D',">","<","*","h","H","+","1","2","3","4","8","p","d","|","_",".",","]

fig = plt.figure(1,figsize=(8,3.6))
plt.clf()
ax = fig.gca()
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('[Local:Remote memory access ratio]')
ax.set_ylabel('Performance [GB/sec]')

nx = 100000
xmin = 0
xmax = 3
ymin = 10 / scalingFactorForRoofs
ymax = 10000 / scalingFactorForRoofs

ax.set_xlim(10**xmin, 10**xmax)
ax.set_ylim(ymin, ymax)

ixx = int(nx*0.02)
xlim = ax.get_xlim()
ylim = ax.get_ylim()

scomp_x_elbow = []
scomp_ix_elbow = []
smem_x_elbow = []
smem_ix_elbow = []

scomp_x_elbow80 = []
scomp_ix_elbow80 = []
smem_x_elbow80 = []
smem_ix_elbow80 = []

x = np.logspace(xmin,xmax,nx)
for roof in scomproofs:
    for ix in range(1,nx):
        if smemroofs[0] * x[ix] >= roof and smemroofs[0] * x[ix-1] < roof:
            scomp_x_elbow.append(x[ix-1])
            scomp_ix_elbow.append(ix-1)
            break
        if smemroofs[0] * x[ix] >= roof and smemroofs[0] * x[ix-1] < roof:
            scomp_x_elbow.append(x[ix-1])
            scomp_ix_elbow.append(ix-1)
            break


for roof in smemroofs:
    for ix in range(1,nx):
        if (scomproofs[0] <= roof * x[ix] and scomproofs[0] > roof * x[ix-1]):
            smem_x_elbow.append(x[ix-1])
            smem_ix_elbow.append(ix-1)
            break

for i in range(0,len(scomproofs)):
    roof = scomproofs[i]
    y = np.ones(len(x)) * roof / scalingFactorForRoofs
    ax.plot(x[scomp_ix_elbow[i]:],y[scomp_ix_elbow[i]:],c='k',ls='-',lw='2')

for i in range(0,len(smemroofs)):
    roof = smemroofs[i]
    y = x * roof / scalingFactorForRoofs

    ax.plot(x[:smem_ix_elbow[i]+1],y[:smem_ix_elbow[i]+1],c=colors[i],ls='-',lw='2')
    ax.vlines(x=x[smem_ix_elbow[i]+1], ymin=ymin, ymax=y[smem_ix_elbow[i]+1], color=colors[i], linestyle='--')
    #print("smem_ix_elbow[i]:",smem_ix_elbow[i],", x:",x[smem_ix_elbow[i]],x[smem_ix_elbow[i]+1])
    #print("ymin:",ymin, "ymax:",y[smem_ix_elbow[i]+1])
ax.grid(True)
marker_handles = list()


for roof in scomproofs:
    ax.text(x[-ixx],roof/scalingFactorForRoofs,
            scomp_roof_name[scomproofs.index(roof)] + ': ' + '{0:.1f}'.format(float(roof)/scalingFactorForRoofs) + 'GB/s',
            horizontalalignment='right',
            verticalalignment='bottom')
c=0
for roof in smemroofs:
    ang = np.arctan(np.log10(xlim[1]/xlim[0]) / np.log10(ylim[1]/ylim[0])
                    * fig.get_size_inches()[1]/fig.get_size_inches()[0] )

    ax.text(x[ixx],x[ixx]*roof/scalingFactorForRoofs*(1+0.25*np.sin(ang)**2),
            smem_roof_name[smemroofs.index(roof)] + ' ' + '{0:.1f}'.format(float(roof)/scalingFactorForRoofs) + ' GB/s',
            horizontalalignment='left',
            verticalalignment='bottom',
            color=colors[c],
            rotation=180/np.pi*ang)

    ax.text(x[smem_ix_elbow[c]],ymin*3,
            'L:R=' + '{0:.1f}'.format(float(x[smem_ix_elbow[c]+1])) ,
            horizontalalignment='left',
            verticalalignment='bottom',
            color=colors[c],
            rotation=90)
    c=c+1

#leg1 = plt.legend(handles = marker_handles,loc=4, ncol=1)

#ax.add_artist(leg1)

#patch_handles = list()
#
#patch_handles.append(mpatches.Patch(color=colors[0],label = 'L1'))
#patch_handles.append(mpatches.Patch(color=colors[1],label = 'L2'))
#patch_handles.append(mpatches.Patch(color=colors[2],label = 'HBM'))

#leg2 = plt.legend(handles = patch_handles,loc='lower right',bbox_to_anchor = (0.8,0),scatterpoints = 1)

#ax.text(xlim[0]*1.1,ylim[1]/1.1,'Memory-Memory Roofline per GPU',horizontalalignment='left',verticalalignment='top')


##apps: cosmoflow 44
#ax.vlines(x=2, ymin=ymin, ymax=20, color='orange', linestyle='-')
#ax.vlines(x=477, ymin=ymin, ymax=y[smem_ix_elbow[1]+1], color='green', linestyle='-')

#ax.grid(b=True, which='major', color='grey', linestyle='-')
#ax.grid(b=True, which='minor', color='grey', linestyle='--')




plt.savefig('memory_roofline_bisection.pdf')



