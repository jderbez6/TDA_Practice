
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
            return(f"No es continua, el abierto {a} no tiene preimagen en la topología del dominio")
            
    return("Es continua")

D = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
I = [0, 1, 4, 9 ,16]

t_d = [[0], [-3,-1, 1, 3], [-4, -2, 2, 4], [-3, -1, 0, 1, 3], [-4, -2, 0, 2, 4], [-4, -3, -2, -1, 1, 2, 3, 4], [-4, -3, -2, -1, 0, 1, 2, 3, 4]]
t_i = [[0], [1, 9], [4, 16], [0, 1, 9], [0, 4, 16], [1, 4, 9, 16], [0, 1, 4, 9, 16]]


def f(x):
  return -x

t_d = [[-1],[-2],[-3],[-4],[0],[1],[2],[3],[4],[-1,-2],[-1,-3],[-2,-3],[-1,-4],[-2,-4],[-3,-4],[-1,0],[-2,0],[-3,0],[-4,0],[-1,1],[-2,1],[-3,1],[-4,1],[0,1],[-1,2],[-2,2],[-3,2],[-4,2],[0,2],[1,2],[-1,3],[-2,3],[-3,3],[-4,3],[0,3],[1,3],[2,3],[-1,4],[-2,4],[-3,4],[-4,4],[0,4],[1,4],[2,4],[3,4],[-1,-2,-3],[-1,-2,-4],[-1,-3,-4],[-2,-3,-4],[-1,-2,0],[-1,-3,0],[-2,-3,0],[-1,-4,0],[-2,-4,0],[-3,-4,0],[-1,-2,1],[-1,-3,1],[-2,-3,1],[-1,-4,1],[-2,-4,1],[-3,-4,1],[-1,0,1],[-2,0,1],[-3,0,1],[-4,0,1],[-1,-2,2],[-1,-3,2],[-2,-3,2],[-1,-4,2],[-2,-4,2],[-3,-4,2],[-1,0,2],[-2,0,2],[-3,0,2],[-4,0,2],[-1,1,2],[-2,1,2],[-3,1,2],[-4,1,2],[0,1,2],[-1,-2,3],[-1,-3,3],[-2,-3,3],[-1,-4,3],[-2,-4,3],[-3,-4,3],[-1,0,3],[-2,0,3],[-3,0,3],[-4,0,3],[-1,1,3],[-2,1,3],[-3,1,3],[-4,1,3],[0,1,3],[-1,2,3],[-2,2,3],[-3,2,3],[-4,2,3],[0,2,3],[1,2,3],[-1,-2,4],[-1,-3,4],[-2,-3,4],[-1,-4,4],[-2,-4,4],[-3,-4,4],[-1,0,4],[-2,0,4],[-3,0,4],[-4,0,4],[-1,1,4],[-2,1,4],[-3,1,4],[-4,1,4],[0,1,4],[-1,2,4],[-2,2,4],[-3,2,4],[-4,2,4],[0,2,4],[1,2,4],[-1,3,4],[-2,3,4],[-3,3,4],[-4,3,4],[0,3,4],[1,3,4],[2,3,4],[-1,-2,-3,-4],[-1,-2,-3,0],[-1,-2,-4,0],[-1,-3,-4,0],[-2,-3,-4,0],[-1,-2,-3,1],[-1,-2,-4,1],[-1,-3,-4,1],[-2,-3,-4,1],[-1,-2,0,1],[-1,-3,0,1],[-2,-3,0,1],[-1,-4,0,1],[-2,-4,0,1],[-3,-4,0,1],[-1,-2,-3,2],[-1,-2,-4,2],[-1,-3,-4,2],[-2,-3,-4,2],[-1,-2,0,2],[-1,-3,0,2],[-2,-3,0,2],[-1,-4,0,2],[-2,-4,0,2],[-3,-4,0,2],[-1,-2,1,2],[-1,-3,1,2],[-2,-3,1,2],[-1,-4,1,2],[-2,-4,1,2],[-3,-4,1,2],[-1,0,1,2],[-2,0,1,2],[-3,0,1,2],[-4,0,1,2],[-1,-2,-3,3],[-1,-2,-4,3],[-1,-3,-4,3],[-2,-3,-4,3],[-1,-2,0,3],[-1,-3,0,3],[-2,-3,0,3],[-1,-4,0,3],[-2,-4,0,3],[-3,-4,0,3],[-1,-2,1,3],[-1,-3,1,3],[-2,-3,1,3],[-1,-4,1,3],[-2,-4,1,3],[-3,-4,1,3],[-1,0,1,3],[-2,0,1,3],[-3,0,1,3],[-4,0,1,3],[-1,-2,2,3],[-1,-3,2,3],[-2,-3,2,3],[-1,-4,2,3],[-2,-4,2,3],[-3,-4,2,3],[-1,0,2,3],[-2,0,2,3],[-3,0,2,3],[-4,0,2,3],[-1,1,2,3],[-2,1,2,3],[-3,1,2,3],[-4,1,2,3],[0,1,2,3],[-1,-2,-3,4],[-1,-2,-4,4],[-1,-3,-4,4],[-2,-3,-4,4],[-1,-2,0,4],[-1,-3,0,4],[-2,-3,0,4],[-1,-4,0,4],[-2,-4,0,4],[-3,-4,0,4],[-1,-2,1,4],[-1,-3,1,4],[-2,-3,1,4],[-1,-4,1,4],[-2,-4,1,4],[-3,-4,1,4],[-1,0,1,4],[-2,0,1,4],[-3,0,1,4],[-4,0,1,4],[-1,-2,2,4],[-1,-3,2,4],[-2,-3,2,4],[-1,-4,2,4],[-2,-4,2,4],[-3,-4,2,4],[-1,0,2,4],[-2,0,2,4],[-3,0,2,4],[-4,0,2,4],[-1,1,2,4],[-2,1,2,4],[-3,1,2,4],[-4,1,2,4],[0,1,2,4],[-1,-2,3,4],[-1,-3,3,4],[-2,-3,3,4],[-1,-4,3,4],[-2,-4,3,4],[-3,-4,3,4],[-1,0,3,4],[-2,0,3,4],[-3,0,3,4],[-4,0,3,4],[-1,1,3,4],[-2,1,3,4],[-3,1,3,4],[-4,1,3,4],[0,1,3,4],[-1,2,3,4],[-2,2,3,4],[-3,2,3,4],[-4,2,3,4],[0,2,3,4],[1,2,3,4],[-1,-2,-3,-4,0],[-1,-2,-3,-4,1],[-1,-2,-3,0,1],[-1,-2,-4,0,1],[-1,-3,-4,0,1],[-2,-3,-4,0,1],[-1,-2,-3,-4,2],[-1,-2,-3,0,2],[-1,-2,-4,0,2],[-1,-3,-4,0,2],[-2,-3,-4,0,2],[-1,-2,-3,1,2],[-1,-2,-4,1,2],[-1,-3,-4,1,2],[-2,-3,-4,1,2],[-1,-2,0,1,2],[-1,-3,0,1,2],[-2,-3,0,1,2],[-1,-4,0,1,2],[-2,-4,0,1,2],[-3,-4,0,1,2],[-1,-2,-3,-4,3],[-1,-2,-3,0,3],[-1,-2,-4,0,3],[-1,-3,-4,0,3],[-2,-3,-4,0,3],[-1,-2,-3,1,3],[-1,-2,-4,1,3],[-1,-3,-4,1,3],[-2,-3,-4,1,3],[-1,-2,0,1,3],[-1,-3,0,1,3],[-2,-3,0,1,3],[-1,-4,0,1,3],[-2,-4,0,1,3],[-3,-4,0,1,3],[-1,-2,-3,2,3],[-1,-2,-4,2,3],[-1,-3,-4,2,3],[-2,-3,-4,2,3],[-1,-2,0,2,3],[-1,-3,0,2,3],[-2,-3,0,2,3],[-1,-4,0,2,3],[-2,-4,0,2,3],[-3,-4,0,2,3],[-1,-2,1,2,3],[-1,-3,1,2,3],[-2,-3,1,2,3],[-1,-4,1,2,3],[-2,-4,1,2,3],[-3,-4,1,2,3],[-1,0,1,2,3],[-2,0,1,2,3],[-3,0,1,2,3],[-4,0,1,2,3],[-1,-2,-3,-4,4],[-1,-2,-3,0,4],[-1,-2,-4,0,4],[-1,-3,-4,0,4],[-2,-3,-4,0,4],[-1,-2,-3,1,4],[-1,-2,-4,1,4],[-1,-3,-4,1,4],[-2,-3,-4,1,4],[-1,-2,0,1,4],[-1,-3,0,1,4],[-2,-3,0,1,4],[-1,-4,0,1,4],[-2,-4,0,1,4],[-3,-4,0,1,4],[-1,-2,-3,2,4],[-1,-2,-4,2,4],[-1,-3,-4,2,4],[-2,-3,-4,2,4],[-1,-2,0,2,4],[-1,-3,0,2,4],[-2,-3,0,2,4],[-1,-4,0,2,4],[-2,-4,0,2,4],[-3,-4,0,2,4],[-1,-2,1,2,4],[-1,-3,1,2,4],[-2,-3,1,2,4],[-1,-4,1,2,4],[-2,-4,1,2,4],[-3,-4,1,2,4],[-1,0,1,2,4],[-2,0,1,2,4],[-3,0,1,2,4],[-4,0,1,2,4],[-1,-2,-3,3,4],[-1,-2,-4,3,4],[-1,-3,-4,3,4],[-2,-3,-4,3,4],[-1,-2,0,3,4],[-1,-3,0,3,4],[-2,-3,0,3,4],[-1,-4,0,3,4],[-2,-4,0,3,4],[-3,-4,0,3,4],[-1,-2,1,3,4],[-1,-3,1,3,4],[-2,-3,1,3,4],[-1,-4,1,3,4],[-2,-4,1,3,4],[-3,-4,1,3,4],[-1,0,1,3,4],[-2,0,1,3,4],[-3,0,1,3,4],[-4,0,1,3,4],[-1,-2,2,3,4],[-1,-3,2,3,4],[-2,-3,2,3,4],[-1,-4,2,3,4],[-2,-4,2,3,4],[-3,-4,2,3,4],[-1,0,2,3,4],[-2,0,2,3,4],[-3,0,2,3,4],[-4,0,2,3,4],[-1,1,2,3,4],[-2,1,2,3,4],[-3,1,2,3,4],[-4,1,2,3,4],[0,1,2,3,4],[-1,-2,-3,-4,0,1],[-1,-2,-3,-4,0,2],[-1,-2,-3,-4,1,2],[-1,-2,-3,0,1,2],[-1,-2,-4,0,1,2],[-1,-3,-4,0,1,2],[-2,-3,-4,0,1,2],[-1,-2,-3,-4,0,3],[-1,-2,-3,-4,1,3],[-1,-2,-3,0,1,3],[-1,-2,-4,0,1,3],[-1,-3,-4,0,1,3],[-2,-3,-4,0,1,3],[-1,-2,-3,-4,2,3],[-1,-2,-3,0,2,3],[-1,-2,-4,0,2,3],[-1,-3,-4,0,2,3],[-2,-3,-4,0,2,3],[-1,-2,-3,1,2,3],[-1,-2,-4,1,2,3],[-1,-3,-4,1,2,3],[-2,-3,-4,1,2,3],[-1,-2,0,1,2,3],[-1,-3,0,1,2,3],[-2,-3,0,1,2,3],[-1,-4,0,1,2,3],[-2,-4,0,1,2,3],[-3,-4,0,1,2,3],[-1,-2,-3,-4,0,4],[-1,-2,-3,-4,1,4],[-1,-2,-3,0,1,4],[-1,-2,-4,0,1,4],[-1,-3,-4,0,1,4],[-2,-3,-4,0,1,4],[-1,-2,-3,-4,2,4],[-1,-2,-3,0,2,4],[-1,-2,-4,0,2,4],[-1,-3,-4,0,2,4],[-2,-3,-4,0,2,4],[-1,-2,-3,1,2,4],[-1,-2,-4,1,2,4],[-1,-3,-4,1,2,4],[-2,-3,-4,1,2,4],[-1,-2,0,1,2,4],[-1,-3,0,1,2,4],[-2,-3,0,1,2,4],[-1,-4,0,1,2,4],[-2,-4,0,1,2,4],[-3,-4,0,1,2,4],[-1,-2,-3,-4,3,4],[-1,-2,-3,0,3,4],[-1,-2,-4,0,3,4],[-1,-3,-4,0,3,4],[-2,-3,-4,0,3,4],[-1,-2,-3,1,3,4],[-1,-2,-4,1,3,4],[-1,-3,-4,1,3,4],[-2,-3,-4,1,3,4],[-1,-2,0,1,3,4],[-1,-3,0,1,3,4],[-2,-3,0,1,3,4],[-1,-4,0,1,3,4],[-2,-4,0,1,3,4],[-3,-4,0,1,3,4],[-1,-2,-3,2,3,4],[-1,-2,-4,2,3,4],[-1,-3,-4,2,3,4],[-2,-3,-4,2,3,4],[-1,-2,0,2,3,4],[-1,-3,0,2,3,4],[-2,-3,0,2,3,4],[-1,-4,0,2,3,4],[-2,-4,0,2,3,4],[-3,-4,0,2,3,4],[-1,-2,1,2,3,4],[-1,-3,1,2,3,4],[-2,-3,1,2,3,4],[-1,-4,1,2,3,4],[-2,-4,1,2,3,4],[-3,-4,1,2,3,4],[-1,0,1,2,3,4],[-2,0,1,2,3,4],[-3,0,1,2,3,4],[-4,0,1,2,3,4],[-1,-2,-3,-4,0,1,2],[-1,-2,-3,-4,0,1,3],[-1,-2,-3,-4,0,2,3],[-1,-2,-3,-4,1,2,3],[-1,-2,-3,0,1,2,3],[-1,-2,-4,0,1,2,3],[-1,-3,-4,0,1,2,3],[-2,-3,-4,0,1,2,3],[-1,-2,-3,-4,0,1,4],[-1,-2,-3,-4,0,2,4],[-1,-2,-3,-4,1,2,4],[-1,-2,-3,0,1,2,4],[-1,-2,-4,0,1,2,4],[-1,-3,-4,0,1,2,4],[-2,-3,-4,0,1,2,4],[-1,-2,-3,-4,0,3,4],[-1,-2,-3,-4,1,3,4],[-1,-2,-3,0,1,3,4],[-1,-2,-4,0,1,3,4],[-1,-3,-4,0,1,3,4],[-2,-3,-4,0,1,3,4],[-1,-2,-3,-4,2,3,4],[-1,-2,-3,0,2,3,4],[-1,-2,-4,0,2,3,4],[-1,-3,-4,0,2,3,4],[-2,-3,-4,0,2,3,4],[-1,-2,-3,1,2,3,4],[-1,-2,-4,1,2,3,4],[-1,-3,-4,1,2,3,4],[-2,-3,-4,1,2,3,4],[-1,-2,0,1,2,3,4],[-1,-3,0,1,2,3,4],[-2,-3,0,1,2,3,4],[-1,-4,0,1,2,3,4],[-2,-4,0,1,2,3,4],[-3,-4,0,1,2,3,4],[-1,-2,-3,-4,0,1,2,3],[-1,-2,-3,-4,0,1,2,4],[-1,-2,-3,-4,0,1,3,4],[-1,-2,-3,-4,0,2,3,4],[-1,-2,-3,-4,1,2,3,4],[-1,-2,-3,0,1,2,3,4],[-1,-2,-4,0,1,2,3,4],[-1,-3,-4,0,1,2,3,4],[-2,-3,-4,0,1,2,3,4],D]

t_d = [[-1],[-2],[-3],[-4],[0],[1],[2],[3],[4],[-1,-2],[-1,-3],[-2,-3],[-1,-4],[-2,-4],[-3,-4],[-1,0],[-2,0],[-3,0],[-4,0],[-1,1],[-2,1],[-3,1],[-4,1],[0,1],[-1,2],[-2,2],[-3,2],[-4,2],[0,2],[1,2],[-1,3],[-2,3],[-3,3],[-4,3],[0,3],[1,3],[2,3],[-1,4],[-2,4],[-3,4],[-4,4],[0,4],[1,4],[2,4],[3,4],[-1,-2,-3],[-1,-2,-4],[-1,-3,-4],[-2,-3,-4],[-1,-2,0],[-1,-3,0],[-2,-3,0],[-1,-4,0],[-2,-4,0],[-3,-4,0],[-1,-2,1],[-1,-3,1],[-2,-3,1],[-1,-4,1],[-2,-4,1],[-3,-4,1],[-1,0,1],[-2,0,1],[-3,0,1],[-4,0,1],[-1,-2,2],[-1,-3,2],[-2,-3,2],[-1,-4,2],[-2,-4,2],[-3,-4,2],[-1,0,2],[-2,0,2],[-3,0,2],[-4,0,2],[-1,1,2],[-2,1,2],[-3,1,2],[-4,1,2],[0,1,2],[-1,-2,3],[-1,-3,3],[-2,-3,3],[-1,-4,3],[-2,-4,3],[-3,-4,3],[-1,0,3],[-2,0,3],[-3,0,3],[-4,0,3],[-1,1,3],[-2,1,3],[-3,1,3],[-4,1,3],[0,1,3],[-1,2,3],[-2,2,3],[-3,2,3],[-4,2,3],[0,2,3],[1,2,3],[-1,-2,4],[-1,-3,4],[-2,-3,4],[-1,-4,4],[-2,-4,4],[-3,-4,4],[-1,0,4],[-2,0,4],[-3,0,4],[-4,0,4],[-1,1,4],[-2,1,4],[-3,1,4],[-4,1,4],[0,1,4],[-1,2,4],[-2,2,4],[-3,2,4],[-4,2,4],[0,2,4],[1,2,4],[-1,3,4],[-2,3,4],[-3,3,4],[-4,3,4],[0,3,4],[1,3,4],[2,3,4],[-1,-2,-3,-4],[-1,-2,-3,0],[-1,-2,-4,0],[-1,-3,-4,0],[-2,-3,-4,0],[-1,-2,-3,1],[-1,-2,-4,1],[-1,-3,-4,1],[-2,-3,-4,1],[-1,-2,0,1],[-1,-3,0,1],[-2,-3,0,1],[-1,-4,0,1],[-2,-4,0,1],[-3,-4,0,1],[-1,-2,-3,2],[-1,-2,-4,2],[-1,-3,-4,2],[-2,-3,-4,2],[-1,-2,0,2],[-1,-3,0,2],[-2,-3,0,2],[-1,-4,0,2],[-2,-4,0,2],[-3,-4,0,2],[-1,-2,1,2],[-1,-3,1,2],[-2,-3,1,2],[-1,-4,1,2],[-2,-4,1,2],[-3,-4,1,2],[-1,0,1,2],[-2,0,1,2],[-3,0,1,2],[-4,0,1,2],[-1,-2,-3,3],[-1,-2,-4,3],[-1,-3,-4,3],[-2,-3,-4,3],[-1,-2,0,3],[-1,-3,0,3],[-2,-3,0,3],[-1,-4,0,3],[-2,-4,0,3],[-3,-4,0,3],[-1,-2,1,3],[-1,-3,1,3],[-2,-3,1,3],[-1,-4,1,3],[-2,-4,1,3],[-3,-4,1,3],[-1,0,1,3],[-2,0,1,3],[-3,0,1,3],[-4,0,1,3],[-1,-2,2,3],[-1,-3,2,3],[-2,-3,2,3],[-1,-4,2,3],[-2,-4,2,3],[-3,-4,2,3],[-1,0,2,3],[-2,0,2,3],[-3,0,2,3],[-4,0,2,3],[-1,1,2,3],[-2,1,2,3],[-3,1,2,3],[-4,1,2,3],[0,1,2,3],[-1,-2,-3,4],[-1,-2,-4,4],[-1,-3,-4,4],[-2,-3,-4,4],[-1,-2,0,4],[-1,-3,0,4],[-2,-3,0,4],[-1,-4,0,4],[-2,-4,0,4],[-3,-4,0,4],[-1,-2,1,4],[-1,-3,1,4],[-2,-3,1,4],[-1,-4,1,4],[-2,-4,1,4],[-3,-4,1,4],[-1,0,1,4],[-2,0,1,4],[-3,0,1,4],[-4,0,1,4],[-1,-2,2,4],[-1,-3,2,4],[-2,-3,2,4],[-1,-4,2,4],[-2,-4,2,4],[-3,-4,2,4],[-1,0,2,4],[-2,0,2,4],[-3,0,2,4],[-4,0,2,4],[-1,1,2,4],[-2,1,2,4],[-3,1,2,4],[-4,1,2,4],[0,1,2,4],[-1,-2,3,4],[-1,-3,3,4],[-2,-3,3,4],[-1,-4,3,4],[-2,-4,3,4],[-3,-4,3,4],[-1,0,3,4],[-2,0,3,4],[-3,0,3,4],[-4,0,3,4],[-1,1,3,4],[-2,1,3,4],[-3,1,3,4],[-4,1,3,4],[0,1,3,4],[-1,2,3,4],[-2,2,3,4],[-3,2,3,4],[-4,2,3,4],[0,2,3,4],[1,2,3,4],[-1,-2,-3,-4,0],[-1,-2,-3,-4,1],[-1,-2,-3,0,1],[-1,-2,-4,0,1],[-1,-3,-4,0,1],[-2,-3,-4,0,1],[-1,-2,-3,-4,2],[-1,-2,-3,0,2],[-1,-2,-4,0,2],[-1,-3,-4,0,2],[-2,-3,-4,0,2],[-1,-2,-3,1,2],[-1,-2,-4,1,2],[-1,-3,-4,1,2],[-2,-3,-4,1,2],[-1,-2,0,1,2],[-1,-3,0,1,2],[-2,-3,0,1,2],[-1,-4,0,1,2],[-2,-4,0,1,2],[-3,-4,0,1,2],[-1,-2,-3,-4,3],[-1,-2,-3,0,3],[-1,-2,-4,0,3],[-1,-3,-4,0,3],[-2,-3,-4,0,3],[-1,-2,-3,1,3],[-1,-2,-4,1,3],[-1,-3,-4,1,3],[-2,-3,-4,1,3],[-1,-2,0,1,3],[-1,-3,0,1,3],[-2,-3,0,1,3],[-1,-4,0,1,3],[-2,-4,0,1,3],[-3,-4,0,1,3],[-1,-2,-3,2,3],[-1,-2,-4,2,3],[-1,-3,-4,2,3],[-2,-3,-4,2,3],[-1,-2,0,2,3],[-1,-3,0,2,3],[-2,-3,0,2,3],[-1,-4,0,2,3],[-2,-4,0,2,3],[-3,-4,0,2,3],[-1,-2,1,2,3],[-1,-3,1,2,3],[-2,-3,1,2,3],[-1,-4,1,2,3],[-2,-4,1,2,3],[-3,-4,1,2,3],[-1,0,1,2,3],[-2,0,1,2,3],[-3,0,1,2,3],[-4,0,1,2,3],[-1,-2,-3,-4,4],[-1,-2,-3,0,4],[-1,-2,-4,0,4],[-1,-3,-4,0,4],[-2,-3,-4,0,4],[-1,-2,-3,1,4],[-1,-2,-4,1,4],[-1,-3,-4,1,4],[-2,-3,-4,1,4],[-1,-2,0,1,4],[-1,-3,0,1,4],[-2,-3,0,1,4],[-1,-4,0,1,4],[-2,-4,0,1,4],[-3,-4,0,1,4],[-1,-2,-3,2,4],[-1,-2,-4,2,4],[-1,-3,-4,2,4],[-2,-3,-4,2,4],[-1,-2,0,2,4],[-1,-3,0,2,4],[-2,-3,0,2,4],[-1,-4,0,2,4],[-2,-4,0,2,4],[-3,-4,0,2,4],[-1,-2,1,2,4],[-1,-3,1,2,4],[-2,-3,1,2,4],[-1,-4,1,2,4],[-2,-4,1,2,4],[-3,-4,1,2,4],[-1,0,1,2,4],[-2,0,1,2,4],[-3,0,1,2,4],[-4,0,1,2,4],[-1,-2,-3,3,4],[-1,-2,-4,3,4],[-1,-3,-4,3,4],[-2,-3,-4,3,4],[-1,-2,0,3,4],[-1,-3,0,3,4],[-2,-3,0,3,4],[-1,-4,0,3,4],[-2,-4,0,3,4],[-3,-4,0,3,4],[-1,-2,1,3,4],[-1,-3,1,3,4],[-2,-3,1,3,4],[-1,-4,1,3,4],[-2,-4,1,3,4],[-3,-4,1,3,4],[-1,0,1,3,4],[-2,0,1,3,4],[-3,0,1,3,4],[-4,0,1,3,4],[-1,-2,2,3,4],[-1,-3,2,3,4],[-2,-3,2,3,4],[-1,-4,2,3,4],[-2,-4,2,3,4],[-3,-4,2,3,4],[-1,0,2,3,4],[-2,0,2,3,4],[-3,0,2,3,4],[-4,0,2,3,4],[-1,1,2,3,4],[-2,1,2,3,4],[-3,1,2,3,4],[-4,1,2,3,4],[0,1,2,3,4],[-1,-2,-3,-4,0,1],[-1,-2,-3,-4,0,2],[-1,-2,-3,-4,1,2],[-1,-2,-3,0,1,2],[-1,-2,-4,0,1,2],[-1,-3,-4,0,1,2],[-2,-3,-4,0,1,2],[-1,-2,-3,-4,0,3],[-1,-2,-3,-4,1,3],[-1,-2,-3,0,1,3],[-1,-2,-4,0,1,3],[-1,-3,-4,0,1,3],[-2,-3,-4,0,1,3],[-1,-2,-3,-4,2,3],[-1,-2,-3,0,2,3],[-1,-2,-4,0,2,3],[-1,-3,-4,0,2,3],[-2,-3,-4,0,2,3],[-1,-2,-3,1,2,3],[-1,-2,-4,1,2,3],[-1,-3,-4,1,2,3],[-2,-3,-4,1,2,3],[-1,-2,0,1,2,3],[-1,-3,0,1,2,3],[-2,-3,0,1,2,3],[-1,-4,0,1,2,3],[-2,-4,0,1,2,3],[-3,-4,0,1,2,3],[-1,-2,-3,-4,0,4],[-1,-2,-3,-4,1,4],[-1,-2,-3,0,1,4],[-1,-2,-4,0,1,4],[-1,-3,-4,0,1,4],[-2,-3,-4,0,1,4],[-1,-2,-3,-4,2,4],[-1,-2,-3,0,2,4],[-1,-2,-4,0,2,4],[-1,-3,-4,0,2,4],[-2,-3,-4,0,2,4],[-1,-2,-3,1,2,4],[-1,-2,-4,1,2,4],[-1,-3,-4,1,2,4],[-2,-3,-4,1,2,4],[-1,-2,0,1,2,4],[-1,-3,0,1,2,4],[-2,-3,0,1,2,4],[-1,-4,0,1,2,4],[-2,-4,0,1,2,4],[-3,-4,0,1,2,4],[-1,-2,-3,-4,3,4],[-1,-2,-3,0,3,4],[-1,-2,-4,0,3,4],[-1,-3,-4,0,3,4],[-2,-3,-4,0,3,4],[-1,-2,-3,1,3,4],[-1,-2,-4,1,3,4],[-1,-3,-4,1,3,4],[-2,-3,-4,1,3,4],[-1,-2,0,1,3,4],[-1,-3,0,1,3,4],[-2,-3,0,1,3,4],[-1,-4,0,1,3,4],[-2,-4,0,1,3,4],[-3,-4,0,1,3,4],[-1,-2,-3,2,3,4],[-1,-2,-4,2,3,4],[-1,-3,-4,2,3,4],[-2,-3,-4,2,3,4],[-1,-2,0,2,3,4],[-1,-3,0,2,3,4],[-2,-3,0,2,3,4],[-1,-4,0,2,3,4],[-2,-4,0,2,3,4],[-3,-4,0,2,3,4],[-1,-2,1,2,3,4],[-1,-3,1,2,3,4],[-2,-3,1,2,3,4],[-1,-4,1,2,3,4],[-2,-4,1,2,3,4],[-3,-4,1,2,3,4],[-1,0,1,2,3,4],[-2,0,1,2,3,4],[-3,0,1,2,3,4],[-4,0,1,2,3,4],[-1,-2,-3,-4,0,1,2],[-1,-2,-3,-4,0,1,3],[-1,-2,-3,-4,0,2,3],[-1,-2,-3,-4,1,2,3],[-1,-2,-3,0,1,2,3],[-1,-2,-4,0,1,2,3],[-1,-3,-4,0,1,2,3],[-2,-3,-4,0,1,2,3],[-1,-2,-3,-4,0,1,4],[-1,-2,-3,-4,0,2,4],[-1,-2,-3,-4,1,2,4],[-1,-2,-3,0,1,2,4],[-1,-2,-4,0,1,2,4],[-1,-3,-4,0,1,2,4],[-2,-3,-4,0,1,2,4],[-1,-2,-3,-4,0,3,4],[-1,-2,-3,-4,1,3,4],[-1,-2,-3,0,1,3,4],[-1,-2,-4,0,1,3,4],[-1,-3,-4,0,1,3,4],[-2,-3,-4,0,1,3,4],[-1,-2,-3,-4,2,3,4],[-1,-2,-3,0,2,3,4],[-1,-2,-4,0,2,3,4],[-1,-3,-4,0,2,3,4],[-2,-3,-4,0,2,3,4],[-1,-2,-3,1,2,3,4],[-1,-2,-4,1,2,3,4],[-1,-3,-4,1,2,3,4],[-2,-3,-4,1,2,3,4],[-1,-2,0,1,2,3,4],[-1,-3,0,1,2,3,4],[-2,-3,0,1,2,3,4],[-1,-4,0,1,2,3,4],[-2,-4,0,1,2,3,4],[-3,-4,0,1,2,3,4],[-1,-2,-3,-4,0,1,2,3],[-1,-2,-3,-4,0,1,2,4],[-1,-2,-3,-4,0,1,3,4],[-1,-2,-3,-4,0,2,3,4],[-1,-2,-3,-4,1,2,3,4],[-1,-2,-3,0,1,2,3,4],[-1,-2,-4,0,1,2,3,4],[-1,-3,-4,0,1,2,3,4],[-2,-3,-4,0,1,2,3,4],D]

t_ds = []
for b in t_d:
    b.sort()
    t_ds.append(b)

topo_continua(f, t_ds, t_ds, D, D)