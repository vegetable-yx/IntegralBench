import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the first modulus: sqrt(3)/2
k1 = mp.sqrt(3) / 2

# Calculate the second modulus: 0.5
k2 = 0.5

# Compute complete elliptic integral of the first kind at k1
K1 = mp.ellipk(k1)

# Compute complete elliptic integral of the first kind at k2
K2 = mp.ellipk(k2)

# Multiply by 2*pi as per the expression
result = 2 * mp.pi * K1 * K2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))