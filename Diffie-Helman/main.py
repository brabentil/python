import random

def power_mod(base, exponent, mod):
    """Computes (base^exponent) % mod using fast modular exponentiation."""
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result

# Step 1: Publicly known values (prime number and base)
p = 23  # A small prime number
g = 5   # A primitive root modulo p

# Step 2: Private keys (randomly chosen)
a = random.randint(1, p-1)  # Alice's private key
b = random.randint(1, p-1)  # Bob's private key

# Step 3: Compute public keys
A = power_mod(g, a, p)  # Alice's public key
B = power_mod(g, b, p)  # Bob's public key

# Step 4: Compute shared secret keys
S_Alice = power_mod(B, a, p)  # Alice computes shared secret
S_Bob = power_mod(A, b, p)  # Bob computes shared secret

# Step 5: Verify if both keys are the same
print("Prime number (p):", p)
print("Base (g):", g)
print("Alice's Private Key:", a)
print("Bob's Private Key:", b)
print("Alice's Public Key:", A)
print("Bob's Public Key:", B)
print("Shared Secret Key (Alice):", S_Alice)
print("Shared Secret Key (Bob):", S_Bob)

assert S_Alice == S_Bob, "Key exchange failed!"
print("Key exchange successful! Shared secret key is:", S_Alice)
