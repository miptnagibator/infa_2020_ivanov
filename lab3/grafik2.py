import numpy as np
import matplotlib.pyplot as plt

# dots and errors
I_1 = [300,
278,
258,
240,
218,
200,
180,
160,
130,
100
]

I_2 = [300,
278,
262,
242,
220,
190,
170,
150,
130,
110
]

I_3 = [300,
278,
262,
242,
222,
200,
178,
160,
130,
110
]

U_1 = [640,
592,
552,
512,
463,
424,
385,
340,
278,
212,
]

U_2 = [955,
884,
830,
764,
699,
603,
540,
476,
416,
347,
]

U_3 = [1601,
1474,
1388,
1279,
1170,
1053,
940,
844,
693,
576,
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
    majorx_ticks = np.arange(0, 400, 20)
    minorx_ticks = np.arange(0, 400, 2)
    majory_ticks = np.arange(0, 1650, 200)
    minory_ticks = np.arange(0, 1650, 20)
    ax.set_xticks(majorx_ticks)
    ax.set_xticks(minorx_ticks, minor=True)
    ax.set_yticks(majory_ticks)
    ax.set_yticks(minory_ticks, minor=True)
    # and a corresponding grid ax.grid(which='both')
    #  or if you want differnet settings for the grids:
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
govno()

plt.errorbar(I_1, U_1, xerr=0.75, yerr=0.07, ls='none', color='red')
plt.errorbar(I_2, U_2, xerr=0.75, yerr=0.07, ls='none', color='green')
plt.errorbar(I_3, U_3, xerr=0.75, yerr=0.07, ls='none', color='blue')
# line functions
p1 = np.polyfit(I_1, U_1, deg=1)
p1_f = np.poly1d(p1)
p2 = np.polyfit(I_2, U_2, deg=1)
p2_f = np.poly1d(p2)
p3 = np.polyfit(I_3, U_3, deg=1)
p3_f = np.poly1d(p3)
# lines
I1 = np.arange(100, 300, 0.01)
I2 = np.arange(110, 300, 0.01)
I3 = np.arange(100, 300, 0.01)
plt.plot(I1, p1_f(I1), label=r'$U_1(I), L = 20 cm$', color='red', linewidth = 2)
plt.plot(I2, p2_f(I2), label=r'$U_2(I), L = 30 cm$', color='green', linewidth = 2)
plt.plot(I3, p3_f(I3), label=r'$U_3(I), L = 50 cm$', color='blue', linewidth = 2)
# grid and labels

plt.legend(loc='best', fontsize=12)
plt.xlabel(r'$I, mA$', fontsize=12)
plt.ylabel(r'$U, mV$', fontsize=12)

plt.show()