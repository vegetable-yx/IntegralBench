import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi to use in expressions
pi_val = mp.pi

# Compute each term of the expression separately
# Term 1: π³ / 48
term1 = (pi_val ** 3) / 48

# Term 2: π² / 8
term2 = (pi_val ** 2) / 8

# Term 3: π / 2
term3 = pi_val / 2

# Term 4: constant -1
term4 = -1

# Combine all terms: π³/48 - π²/8 + π/2 - 1
result = term1 - term2 + term3 + term4

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))