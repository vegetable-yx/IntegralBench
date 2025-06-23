import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant fraction 1575/128
fraction = mp.mpf(1575) / mp.mpf(128)

# Compute zeta(3) using mpmath's zeta function
zeta3 = mp.zeta(3)

# Multiply to get the final result
result = fraction * zeta3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))