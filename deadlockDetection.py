import numpy as np 

#*************************************************
# Allocation Matrix 
alloc = np.array([
        [0,1,0],
        [2,0,0], 
        [3,0,3],
        [2,1,1],
        [0,0,2]
        ])

# request Matrix 
request = np.array([
        [0,0,0],
        [2,0,2], 
        [0,0,0],
        [1,0,0],
        [0,0,2]
        ])

avail = np.array([0,0,0]) # Available Resources  size 1xm

#****************************************************

def infor(f):
    s = ''
    for i in range(len(f)):
        if f[i] == 0:
            s += ' F'
        else:
            s += ' T'
    return 'Finish =' + s

def is_lessOrEqual(vec1, vec2):
    for i in range(len(vec1)):
        if vec1[i]>vec2[i]:
            return False
    return True


n = alloc.shape[0] # Number of processes 
m = alloc.shape[1] # Number of resources 

finish = np.zeros(n)

print('1) a) work = avail = ', avail)
w = avail
print('   b) ')
for i in range(n):
    if is_lessOrEqual( np.zeros(m), alloc[i]) or is_lessOrEqual(np.zeros(m), request[i]) :
        finish[i] = 0
    else:
        finish[i] = 1

print(infor(finish))
order = ''
while (True):
    flag = 0
    for i in range(n):
        if finish[i]==0 and is_lessOrEqual(request[i],w):
            flag = 1
            print('\n2) Found ', i, '\nFinish[',i,'] = false,\n request[',i,'] (=',request[i],') <= work (=',w,')')
            print('3) w = w + alloc[i] = ', w, ' + ', alloc[i], ' = ', w+alloc[i])
            # print('finish[',i,'] = true')
            w+=alloc[i]
            finish[i]=1
            order += ' P' + str(i)
            print(infor(finish))
            break
    if flag == 0:
        break
print('Order:', order)

