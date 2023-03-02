
def Pre(f, I, D, E):
    p = []
    for x in D:
        if f(x) in I and f(x) in E:
            p.append(x)

    return p

def f(x):
    y = x**2
    return y


def topo_continua(f, t_d, t_i, I, D):
    for a in t_i:
        if Pre(f, I, D, a) not in t_d:
            return("No es continua")
    return("Es continua")

D = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
I = [0, 1, 4, 9 ,16]

t_d = [[0], [-3,-1, 1, 3], [-4, -2, 2, 4], [-3, -1, 0, 1, 3], [-4, -2, 0, 2, 4], [-4, -3, -2, -1, 1, 2, 3, 4], [-4, -3, -2, -1, 0, 1, 2, 3, 4]]
t_i = [[0], [1, 9], [4, 16], [0, 1, 9], [0, 4, 16], [1, 4, 9, 16], [0, 1, 4, 9, 16]]

topo_continua(f, t_d, t_i, I, D)