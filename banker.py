import numpy as np 

#*************************************************
# Allocation Matrix 
alloc = np.array([
        [0,0,1],
        [1,0,0], 
        [1,3,5],
        [0,6,3],
        [0,0,1]
        ])

# MAX Matrix 
max = np.array([
        [0,0,1],
        [1,7,5], 
        [2,3,5],
        [0,6,5],
        [0,6,5]
        ])

avail = np.array([1,5,2]) # Available Resources  size 1xm

#****************************************************

def is_lessOrEqual(vec1, vec2):
    for i in range(len(vec1)):
        if vec1[i]>vec2[i]:
            return False
    return True

def infor(f):
    s = ''
    for i in range(len(f)):
        if f[i] == 0:
            s += ' F'
        else:
            s += ' T'
    return s


n = alloc.shape[0] # Number of processes 
m = alloc.shape[1] # Number of resources 

need = max - alloc
order = ''


work = avail
finish = np.zeros(n)
print('1) \n init: work = ',avail,'\n  Finish = ', infor(finish))

while(True):
    flag = 0
    for i in range(n):
        if finish[i] == 0 and is_lessOrEqual(need[i], work) :
            flag = 1
            print('\n2) Found i = '+ str(i) + ' : finish[i] = false , \nneed [i] ( = '+ str(need[i]) +' ) <= work ( = '+ str(work) +' )' )
            print('3) work = work + alloc_i = ' + str(work) + ' + ' + str(alloc[i]) + ' = ' + str(work + alloc[i])  )
            print('finish[' +str(i) +'] = true')
            work = work + alloc[i]
            finish[i] = 1
            order += ' P' + str(i)
            print('finish = ', infor(finish))
            break
    if flag == 0:
        break

print('\n Order: ' + order)


