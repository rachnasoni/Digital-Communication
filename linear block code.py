#linear block code short

import numpy as np
G=np.array([[1,0,1],[1,1,0],[0,1,1]])
msg= input("enter message")
message= np.array([int(bit) for bit in msg])
if len(message)==3:
  codeword= np.dot(message,G)%2
  print("messsage: ", message)
  print("codeword: ",codeword)




#Linear block code longer version

import numpy as np
import math
H=np.matrix('1 1 1 1 0 0;1 1 0 0 1 0;1 0 1 0 0 1')
print("input matrix given is")
print(H)

#binary
def bingen(n):
  for i in range(16):
    b=bin(i)[2:]
    l=len(b)
    b=str(0)*(n-l)+b
M=bingen(4)

def HtoG(H):
    n = np.shape(H)[1]
    k = n - np.shape(H)[0]
    P = HtoP(H)
    Ik = np.eye(k)
    G = np.concatenate((Ik,P), axis=1)
    print(" Generator matrix: ")
    print(G.astype(int))
    return G.astype(int)

def HtoP(H):
    n = np.shape(H)[1]
    k = n - np.shape(H)[0]
    PK = H[:,0:n-k]
    print("transpose of parity: ")
    print(PK)
    B = np.transpose(PK)
    print("parity matrix: ")
    print(B.astype(int))
    return B.astype(int)

HtoG(H)

def synH(H):
    Ht = np.transpose(H)
    print("transpose of parity check matrix ")
    print(Ht)
    n = np.shape(Ht)[0]
    k = n - np.shape(Ht)[1]
    Ik = np.eye(n)
    SynTable = np.concatenate((Ik,Ht), axis=1)
    print("syndrome table ")
    print(SynTable)
synH(H)

def gen_cw(msg, gen_mat):
    if len(msg) != gen_mat.shape[0]:
        raise ValueError("Message length must match the number of columns in the generator matrix")
    msg_array = np.array(msg)
    codeword = np.dot(msg_array, gen_mat) % 2
    return codeword.tolist()

gen_mat = np.array([[ 1, 0, 1],[1, 1, 0],[ 0, 1, 1]])

msg = [1,0,1]

codeword = gen_cw(msg, gen_mat)

print("Message:", msg)
print("Codeword:", codeword)
