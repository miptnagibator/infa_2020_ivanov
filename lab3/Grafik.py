import numpy as np
import matplotlib.pyplot as plt

# dots and errors
I_1 = [4.479,
9.01,
13.6,
18.291,
23.304,
18.291,
13.6,
9.01,
4.479,
4.479,
9.01,
13.6,
18.291,
23.304,
18.291,
13.6,
9.01,
4.479,
4.479,
9.01,
13.6,
18.291,
23.304,
18.291,
13.6,
9.01,
4.479,
]


U_1 = y1 = [0.86,
1.75,
2.64,
3.58,
4.57,
3.59,
2.65,
1.74,
0.83,
0.83,
1.72,
2.61,
3.51,
4.48,
3.49,
2.59,
1.68,
0.79,
0.83,
1.73,
2.64,
3.61,
4.56,
3.64,
2.74,
1.81,
0.95,

]

I_2 = [4.479,
9.01,
13.6,
18.291,
23.304,
18.291,
13.6,
9.01,
4.479,
4.479,
9.01,
13.6,
18.291,
23.304,
18.291,
13.6,
9.01,
4.479,
4.479,
9.01,
13.6,
18.291,
23.304,
18.291,
13.6,
9.01,
4.479,
]

U_2 = [
1.11,
2.2,
3.29,
4.39,
5.59,
4.34,
3.14,
1.99,
0.9,
1.08,
2.21,
3.3,
4.4,
5.65,
4.37,
3.21,
2.04,
0.94,
1.1,
2.26,
3.46,
4.65,
5.9,
4.63,
3.43,
2.28,
1.14,

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
    majorx_ticks = np.arange(-3, 35, 2 )
    minorx_ticks = np.arange(-3, 35, 0.2)
    majory_ticks = np.arange(-3, 8 , 0.5)
    minory_ticks = np.arange(-3, 8 , 0.05)
    ax.set_xticks(majorx_ticks)
    ax.set_xticks(minorx_ticks, minor=True)
    ax.set_yticks(majory_ticks)
    ax.set_yticks(minory_ticks, minor=True)
    # and a corresponding grid ax.grid(which='both')
    #  or if you want differnet settings for the grids:
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
govno()

plt.errorbar(I_1, U_1, xerr=0.0, yerr=0.01, ls='none', color='red')
plt.errorbar(I_2, U_2, xerr=0.0, yerr=0.01, ls='none', color='green')
#plt.errorbar(I_3, U_3, xerr=0.75, yerr=0.07, ls='none', color='blue')

# line functions
p1 = np.polyfit(I_1, U_1, deg=1)
p1_f = np.poly1d(p1)
p2 = np.polyfit(I_2, U_2, deg=1)
p2_f = np.poly1d(p2)
#p3 = np.polyfit(I_3, U_3, deg=1)
#p3_f = np.poly1d(p3)
# lines
I1 = np.arange(0, 25, 0.01)
I2 = np.arange(0, 25, 0.01)
I3 = np.arange(100, 300, 0.01)
plt.plot(I1, p1_f(I1), label=r'$Деревянная балка$', color='red', linewidth = 2)
plt.plot(I2, p2_f(I2), label=r'$Металлическая балка$', color='green', linewidth = 2)
#plt.plot(I3, p3_f(I3), label=r'$U_3(I), L = 50 cm$', color='blue', linewidth = 2)
# grid and labels
plt.scatter(I_1,U_1)
plt.scatter(I_2,U_2)
plt.legend(loc='best', fontsize=12)
plt.xlabel(r'$P, N$', fontsize=12)
plt.ylabel(r'$Y_{max}, mm$', fontsize=12)

plt.show()