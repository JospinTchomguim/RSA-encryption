from math import gcd

# fonction pour vérifier si un nombre est premier ou pas
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# fonction pour obtenir une valeur valide pour e
def get_valid_e(p, q):
    t = (p - 1) * (q - 1)
    for i in range(2, t):
        if gcd(i, t) == 1 and is_prime(i):
            return i
    return None

# fonction qui applique l'approche RSA
def RSA(p: int, q: int, message: int):
    # calculons n
    n = p * q

    # sélection de la clé publique e
    e = None
    while not e:
        e_candidate = int(input("Enter a value for e: "))
        if gcd(e_candidate, (p-1)*(q-1)) == 1 and is_prime(e_candidate):
            e = e_candidate
        else:
            #si l'utilisateur entre une valeur de e qui n'est pas valide
            print("Invalid value for e. Please try again.")

    # sélection de la clé privée d
    j = 0
    while True:
        if (j * e) % ((p-1) * (q-1)) == 1:
            d = j
            break
        j += 1

    # Chiffrement en utilisant la clé publique (n, e)
    ct = (message ** e) % n
    print(f"Encrypted message is {ct}\n")
    #print("\n")

    # Déchiffrement en utilisant la clé privée d
    mes = (ct ** d) % n
    print(f"Decrypted message is {mes}")

# Test du programme 
p = 5
q = 17
message = 10
RSA(p, q, message)



