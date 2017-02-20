def answer(xs):
    s = xs


    pos = None
    m = list(i for i in s if i >0)
    lenm = len(m)
    if lenm > 0:
        pos = 1
        for i in m:
            pos = pos*i

    nos = None
    n = list(i for i in s if i <0)
    lenn = len(n)
    if lenn % 2 != 0:
        n.sort()
        nos = n.pop(len(n)-1)
        #nos  = n[0]
        lenn = lenn -1

    if lenn > 0:
        nos = 1
        for i in n:
            nos = nos*i

    zos = None
    z = list(i for i in s if i ==0)
    if len(z) > 0:
        zos = 0

    r = []
    if pos is not None:
        r.append(pos)

    if nos is not None:
        r.append(nos)

    if pos is not None and nos is not None:
        r.append(pos*nos)

    if zos is not None:
        r.append(0)

    m = max(r)
    print m, r
    return str(m)
