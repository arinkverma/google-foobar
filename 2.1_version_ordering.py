#major, minor, revision
lr = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "1"]

def answer(s):
    lr = s
    for i in xrange(len(lr)):
        m = map(int, lr[i].split("."))

        lens = len(m)
        if lens == 2:
            m.append(0)
        elif lens == 1:
            m.append(0)
            m.append(0)

        m.append(lr[i])
        lr[i] = m

    l = lr
    l3 = sorted(l,key=lambda t: len(t[3]))
    l2 = sorted(l3,key=lambda t: t[2])
    l1 = sorted(l2,key=lambda t: t[1])
    l0 = sorted(l1,key=lambda t: t[0])

    r = list(i[3] for i in l0)
    return r


