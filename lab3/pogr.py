import math

I_1 = [10.79, 15.31, 19.72, 24.01, 28.85]

U_1 = y1 = [
146.2**2,
173.9**2,
195.9**2,
215.2**2,
237.7**2,
]

k = 1924
govno = 532.3





def pogr(x,y, k, govno):
    xsrkv = 0
    for i in range(len(x)):
        xsrkv+=x[i]**2
    xsrkv = xsrkv/len(x)
    ysrkv =0
    for i in range(len(y)):
        ysrkv+=(y[i] - govno)**2
    ysrkv = ysrkv/len(y)
    print((ysrkv/xsrkv) - k**2)
    return (1/math.sqrt(len(x)))*math.sqrt( (ysrkv/xsrkv) - k**2 )


print(pogr(I_1, U_1, k, govno))
