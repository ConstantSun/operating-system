import numpy as np 
#*************************************************
requestID = 4     # index of process index
request = np.array([1,0,0]) # request content
# Allocation Matrix 
alloc = np.array([
        [0,1,0],
        [2,0,0], 
        [3,0,1],
        [2,1,1],
        [0,0,2]
        ])
# MAX Matrix 
max = np.array([
        [7,5,3],
        [3,2,2], 
        [9,0,2],
        [2,2,2],
        [4,3,3]
        ])
avail = np.array([3,3,2]) # Available Resources  size 1xm

#****************************************************

# requestID = 2 # index of process index
# request = np.array([1]) # request content
# # Allocation Matrix 
# alloc = np.array([
#         [5],
#         [2],
#         [2]
#         ])
# # MAX Matrix 
# max = np.array([
#        [10],
#        [4],
#        [9]
#         ])
# avail = np.array([3]) # Available Resources  size 1xm


def infor(f):
    s = ''
    for i in range(len(f)):
        if f[i] == 0:
            s += ' F'
        else:
            s += ' T'
    return s

def is_lessOrEqual(vec1, vec2):
    for i in range(len(vec1)):
        if vec1[i]>vec2[i]:
            return False
    return True


n = alloc.shape[0] # Number of processes 
m = alloc.shape[1] # Number of resources 

need = max - alloc
order = ''


if is_lessOrEqual(request, need[requestID]):
    print('1) Request <= need ')

    if is_lessOrEqual(request, avail):
        print('2) req <= avail')
        print('3) pretend: ')
        print('avail = avail - request = ', avail, ' - ', request, ' = ', avail - request)
        print('alloc[', requestID,'] = ', 'alloc[', requestID,'] + request[', requestID, ']', ' = ', alloc[requestID] + request)
        print('need_', requestID, '=need_', requestID, ' - request_', requestID, ' = ', need[requestID] - request)
        avail -= request
        alloc[requestID] += request
        need[requestID] -= request
        print('\n------------------------------------------------------------------------------- \nCall banker algorithm:')

        
        work = avail
        finish = np.zeros(n)
        print('1) \n init: work = avai = ', avail,'\n Finish = ', infor(finish))

        while(True):
            flag = 0
            for i in range(n):
                if finish[i] == 0 and is_lessOrEqual(need[i], work) :
                    flag = 1
                    print('\n2) Found i = '+ str(i) + ' : finish[i] = false , \nneed [i] ( '+ str(need[i]) +' ) <= work ( '+ str(work) +' )' )
                    print('3) work = work + alloc_i = ' + str(work) + ' + ' + str(alloc[i]) + ' = ' + str(work + alloc[i])  )
                    print('finish[' +str(i) +'] = true')
                    work = work + alloc[i]
                    finish[i] = 1
                    order += ' P' + str(i)

                    print('Finish =', infor(finish))
                    break
            if flag == 0:
                break

        print('\n Order: ' + order)
        print('Finish = ', infor(finish))
    else:
        print('Erro : req > available')
else:
    print('Error: request > need ')

