import matplotlib.pyplot as plt
x = [0,
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
]
y1 = [4.918734,
9.786456,
14.663988,
19.297251,
24.246396,
29.16513,
24.246396,
19.297251,
14.663988,
9.786456,
4.918734,
]
#y2 = [0.333 , 1, 1, 1, 1.016, 1.033, 0.967, 0.933]

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
plt.grid()

plt.plot(x, y1,"rs", label=r'$K (AC) $', linewidth = 2)
#plt.plot(x, y2, "bs", label=r'$K (DC)$', linewidth = 2)
plt.legend(loc='best', fontsize=12)
plt.xlabel(r'$lg(f)$', fontsize=12)
plt.ylabel(r'$K$', fontsize=12)

plt.grid()
plt.show()