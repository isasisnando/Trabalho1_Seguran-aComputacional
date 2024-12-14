from encryption import DES_ENCRYPTION, fk, F, switch,first_perm,final_perm

def DES_DECRYPTION(ciphertext, k1,k2):
    
    text = first_perm(ciphertext)
    
    fk2 = fk(text[:4], text[4::], k2)
    
    sw = switch(fk2)
    
    fk1 = fk(sw[:4], sw[4::], k1)
    
    ans = final_perm(fk1)
    
    answer = ""
    for x in ans:
        answer += str(x)
    return answer
