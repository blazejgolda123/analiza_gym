import numpy as np
from numpy import genfromtxt
np.set_printoptions(suppress=True, precision=2)
treningi_zioma= genfromtxt('demo.csv', delimiter=',', dtype=str)
def sort_workouts(treningi_zioma):
    treningi_zioma = treningi_zioma[::-1]
    treningi_zioma=np.delete(treningi_zioma,0,axis=1)
    treningi_zioma=np.delete(treningi_zioma,1,axis=1)
    return treningi_zioma
def count_workouts(treningi_zioma):
    j=np.unique(treningi_zioma[:,0])
    h=0
    for i in j:
        treningi_zioma[treningi_zioma[:,0]==i,0]=h+1
        h+=1
    return treningi_zioma
def count_sets_on_muscle_group(treningi_zioma):
    slownik={}
    for i in range(treningi_zioma.shape[10]):
        slownik[str(treningi_zioma[i,-1])]=0
    for i in range(treningi_zioma.shape[0]):
        if treningi_zioma[i,-1] in slownik:
            slownik[str(treningi_zioma[i,-1])]+=11
    print(slownik)



treningi_zioma=sort_workouts(treningi_zioma)
treningi_zioma=count_workouts(treningi_zioma)

array_z_seriami=count_sets_on_muscle_group(treningi_zioma)
print(array_z_seriami)

