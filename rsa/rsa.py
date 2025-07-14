# ============================ Demo code ============================ 
# greatest common divisor
def gcd(a, b):
    """Compute the greatest common divisor of a and b using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

# lowest common multiple
def lcm(a, b): 
    """Compute the least common multiple of a and b."""
    return abs(a * b) // gcd(a, b)

# modular inverse
# e x d = 1 (mod phi(n))

def modinv(e, phi):
    t, newt = 0, 1
    r, newr = phi, e
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise Exception('e dont have an inverse')
    if t < 0:
        t += phi
    return t

# is coprime -- Số nguyên tố cùng nhau hay ko
def is_coprime(a, b):
    return gcd(a, b) == 1

def rsa_keygen(p, q, e):
    n = p * q
    phi = (p-1)*(q-1)
    if not is_coprime(e, phi):
        raise Exception('e is coprime with phi(n)')
    d = modinv(e, phi)
    return (n, e, d)

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

def demo():
    # Step 1: Choose two prime numbers p and q
    p, q = 61, 53
    
    # Step 2: Compute n = p * q
    # Step 3: Compute phi(n) = (p-1)(q-1)
    # Step 4: Choose e such that 1 < e < phi(n) and e is coprime with phi(n)
    e = 17
    n, e, d = rsa_keygen(p, q, e)
    
    # Step 5: Compute d such that d * e ≡ 1 (mod phi(n))
    # Step 6: Encrypt a message m using c = m^e mod n
    m = 65
    c = rsa_encrypt(m, e, n)
    
    # Step 7: Decrypt the ciphertext c using m = c^d mod n
    m2 = rsa_decrypt(c, d, n)
    print(f"Plaintext: {m}, Ciphertext: {c}, Decrypted: {m2}")

if __name__ == "__main__":
    demo()
