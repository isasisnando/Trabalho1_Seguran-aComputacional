from encryption import DES_ENCRYPTION, fk, F, switch
from Trabalho1_SegurancaComputacional.gen_key import gen, ls_1, p8
from decryption import DES_DECRYPTION

texto = input("Texto, string binaria de 8 bits: ")
chave = input("Chave de 10 bits: ")
k1,k2 = gen(chave)
cipher = DES_ENCRYPTION(texto,k1,k2)
plain = DES_DECRYPTION(cipher,k1,k2)
print(cipher)
print(plain)