import matplotlib.pyplot as plt
x = [0, 2, 3, 4, 5, 6, 6.4, 6.7]
y1 = [1, 1, 1, 1, 1.016, 1.016, 0.967, 0.933]
y2 = [0.333 , 1, 1, 1, 1.016, 1.033, 0.967, 0.933]

def govno():
    import numpy as np
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #major ticks every 20, minor ticks every 5
    majorx_ticks = np.arange(0, 7, 1)
    minorx_ticks = np.arange(0, 7, 0.1 )
    majory_ticks = np.arange(0, 1.1 , 0.2)
    minory_ticks = np.arange(0, 1.1 , 0.02)
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
plt.plot(x, y2, "bs", label=r'$K (DC)$', linewidth = 2)
plt.legend(loc='best', fontsize=12)
plt.xlabel(r'$lg(f)$', fontsize=12)
plt.ylabel(r'$K$', fontsize=12)

plt.grid()
plt.show()