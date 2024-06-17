def multi(g):
    g =  sorted(g)
    wait = 0
    display = ()
    for z in range(len(g)):
        if wait > 0:
            wait -= 1
            continue
        t = g[z]
        n = 1
        for i in range(len(g)):
            if i!= z and t[0] == g[i][0] and t[1] == g[i][1]:
                n += 1
        wait = n - 1
        display = display + ((t[0], n, t[1]),)
    return display