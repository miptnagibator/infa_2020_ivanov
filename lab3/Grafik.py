import numpy as np
import matplotlib.pyplot as plt

# dots and errors
I_1 = [10.79, 15.31, 19.72, 24.01, 28.85]


U_1 = y1 = [
146.2**2,
173.9**2,
195.9**2,
215.2**2,
237.7**2,
]


U_2 = [
171.5,
344,
516.3,
690,
863,
1036,
1212,
1387.4,
1562.8
]

U_3 = [
193.1,
389.4,
581.7,
779.6,
971.4,
1172.2,
1363.5,
1569.1,
1758.3,
]

U_4 = [
213.6,
430.2,
642.4,
862.5,
1071,
1296.3,
1504,
1735.8,
1923.6

]

U_5 = [
235.7,
472.7,
709.1,
945.7,
1183.4,
1421.5,
1659.5,
1899.1,
2137.7,

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
    majorx_ticks = np.arange(0, 31, 5 )
    minorx_ticks = np.arange(0, 31, 0.5)
    majory_ticks = np.arange(0, 220000 , 10000)
    minory_ticks = np.arange(0, 220000 , 1000)
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
'''plt.errorbar(I_1, U_2, xerr=0.0, yerr=0.01, ls='none', color='green')
plt.errorbar(I_1, U_3, xerr=0.0, yerr=0.07, ls='none', color='blue')
plt.errorbar(I_1, U_4, xerr=0.0, yerr=0.07, ls='none', color='yellow')
plt.errorbar(I_1, U_5, xerr=0.0, yerr=0.07, ls='none', color='orange')'''

# line functions
p1 = np.polyfit(I_1, U_1, deg=1)
p1_f = np.poly1d(p1)

'''p2 = np.polyfit(I_1, U_2, deg=1)
p2_f = np.poly1d(p2)
p3 = np.polyfit(I_1, U_3, deg=1)
p3_f = np.poly1d(p3)
p4 = np.polyfit(I_1, U_4, deg=1)
p4_f = np.poly1d(p4)
p5 = np.polyfit(I_1, U_5, deg=1)
p5_f = np.poly1d(p5)
sigma = np.poly'''


print(p1_f)
'''print(p2_f)
print(p3_f)
print(p4_f)
print(p5_f)'''


# lines

I1 = np.arange(0, 31, 0.01)
I2 = np.arange(0, 10, 0.01)
I3 = np.arange(0, 10, 0.01)
I4 = np.arange(0, 10, 0.01)
I5 = np.arange(0, 10, 0.01)

plt.plot(I1, p1_f(I1), label=r'$U^2(T)$', color='red', linewidth = 2)
'''plt.plot(I2, p2_f(I2), label=r'$\nu_(n), T = 15,34 N$', color='green', linewidth = 2)
plt.plot(I3, p3_f(I3), label=r'$\nu_(n), T = 19,72 N$', color='blue', linewidth = 2)
plt.plot(I4, p4_f(I4), label=r'$\nu_(n), T = 24,01 N$', color='orange', linewidth = 2)
plt.plot(I5, p5_f(I5), label=r'$\nu_(n), T = 28,85 N$', color='black', linewidth = 2)'''


# grid and labels
plt.scatter(I_1,U_1)
'''plt.scatter(I_1,U_2)
plt.scatter(I_1,U_3)
plt.scatter(I_1,U_4)
plt.scatter(I_1,U_5)'''


plt.legend(loc='best', fontsize=12)
plt.xlabel(r'$T, N$', fontsize=12)
plt.ylabel(r'$U^2(T), m/s$', fontsize=12)

plt.show()