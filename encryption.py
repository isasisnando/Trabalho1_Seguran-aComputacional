def F(n,key):
    
    #expansion and permutation operation
    E = [4,1,2,3,2,3,4,1]
    
    #xor between the applied expansion operation and the key
    values = []
    for i in range(len(E)):
        aux = int(n[E[i]-1])^(int(key[i]))
        values.append(aux)

    #define S-boxes
    S0 = [[1,0,3,2],
          [3,2,1,0],
          [0,2,1,3],
          [3,1,3,2]]
    
    S1 = [[0,1,2,3],
          [2,0,1,3],
          [3,0,1,0],
          [2,1,0,3]]
    
    #Getting the decimal number that represents each row and column 
    #that represent the bits in the S-box
    row1 = values[0]*2 + values[3]
    column1 = values[1]*2 + values[2]
    row2 = values[4]*2 + values[7]
    column2 = values[5]*2 + values[6]

    output1 = bin(S0[row1][column1])
    # Removing the inital '0b' from the string
    output1 = output1[2::]
    if len(output1) <2:
        output1 = '0' + output1
    
    output2 = bin(S1[row2][column2])
    output2 = output2[2::]
    if len(output2) <2:
        output2 = '0' + output2
   
    
    output = output1 + output2
    final = []
    #Final permutation of the 4 bits produces by the S-boxes
    
    perm = [2,4,3,1]
    for i in range(len(perm)):
        final.append(int(output[perm[i]-1]))
    
    return final

def fk(L, R,k):
    #Mapping operation that will be parameter in Fk function
    # Apply to the right half with key
    f = F(R,k)
    
    new_left = []
    new_right = R  
    for i in range(len(L)):
        new_left.append(int(L[i])^f[i])
    
    final = []
    for x in new_left:
        final.append(x)
    for x in new_right:
        final.append(int(x))
    return final

def switch(lst):
    new_lst = []
    for i in range(len(lst)//2, len(lst)):
        new_lst.append(lst[i])
    for i in range(len(lst)//2):
        new_lst.append(lst[i])
    return new_lst

def first_perm(plaintext):
    ip = [2,6,3,1,4,8,5,7]
    #Apply initial permutation to plaintext and generate text that will undergo the operations
    text = []
    for i in range(len(ip)):
        text.append(int(plaintext[ip[i]-1]))
    return text

def final_perm(text):
    ip_inv = [4,1,3,5,7,2,8,6]
    
    answer = []
    for i in range(len(ip_inv)):
        answer.append(text[ip_inv[i]-1])
    return answer

def DES_ENCRYPTION(plaintext, k1, k2):
    # IP'(Fk2(Switch(Fk1(IP))))
    
    #initial permutation 
    text = first_perm(plaintext)
    
    #Apply first Fk function with k1 as a parameter
    fk1 = fk(text[:4], text[4::],k1)
    
    
    text = switch(fk1)
    
    
    fk2 = fk(text[:4], text[4::], k2)
    
    #inverse and final permutation
    
    lista = final_perm(fk2)
    answer = ""
    for x in lista:
        answer += str(x)
    return answer



