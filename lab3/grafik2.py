import numpy as np
import matplotlib.pyplot as plt

# dots and errors
I_1 = [0,
0.301158301,
0.563706564,
0.787644788,
1.027027027,
1.258687259,
1.034749035,
0.795366795,
0.571428571,
0.316602317,
0.015444015,
0.316602317,
0.571428571,
0.787644788,
1.027027027,
1.250965251,
1.019305019,
0.787644788,
0.579150579,
0.308880309,
0.023166023,

]


U_1 = y1 = [0,
4.867722,
9.745254,
14.378517,
19.327662,
24.246396,
19.327662,
14.378517,
9.745254,
4.867722,
0,
4.867722,
9.745254,
14.378517,
19.327662,
24.246396,
19.327662,
14.378517,
9.745254,
4.867722,
0
]


'''fig, ax = plt.subplots()
ax.minorticks_on()

ax.grid(which='major',
        color = 'b',
        linewidth = 1)

ax.grid(which='minor',
        color = 'b',
        linestyle = ':')

fig.set_figwidth(12)
fig.set_figheight(60)'''

def govno():
    import numpy as np
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #major ticks every 20, minor ticks every 5
    majorx_ticks = np.arange(0, 2, 0.1)
    minorx_ticks = np.arange(0, 2, 0.02 )
    majory_ticks = np.arange(0, 30 , 5)
    minory_ticks = np.arange(0, 30 , 1)
    ax.set_xticks(majorx_ticks)
    ax.set_xticks(minorx_ticks, minor=True)
    ax.set_yticks(majory_ticks)
    ax.set_yticks(minory_ticks, minor=True)
    # and a corresponding grid ax.grid(which='both')
    #  or if you want differnet settings for the grids:
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
govno()

plt.errorbar(I_1, U_1, xerr=0.015, yerr=0.1, ls='none', color='red')
#plt.errorbar(I_2, U_2, xerr=0.75, yerr=0.07, ls='none', color='green')
#plt.errorbar(I_3, U_3, xerr=0.75, yerr=0.07, ls='none', color='blue')

# line functions
p1 = np.polyfit(I_1, U_1, deg=1)
p1_f = np.poly1d(p1)
#p2 = np.polyfit(I_2, U_2, deg=1)
#p2_f = np.poly1d(p2)
#p3 = np.polyfit(I_3, U_3, deg=1)
#p3_f = np.poly1d(p3)
# lines
I1 = np.arange(0, 1.3, 0.01)
I2 = np.arange(110, 300, 0.01)
I3 = np.arange(100, 300, 0.01)
plt.plot(I1, p1_f(I1), label=r'$P(\Delta l)$', color='red', linewidth = 2)
#plt.plot(I2, p2_f(I2), label=r'$U_2(I), L = 30 cm$', color='green', linewidth = 2)
#plt.plot(I3, p3_f(I3), label=r'$U_3(I), L = 50 cm$', color='blue', linewidth = 2)
# grid and labels
plt.scatter(I_1,U_1)
plt.legend(loc='best', fontsize=12)
plt.xlabel(r'$\Delta l, mm$', fontsize=12)
plt.ylabel(r'$P, N$', fontsize=12)

plt.show()