import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute the Hurwitz zeta function at s=3 for a=1/4
zeta1 = mp.zeta(3, 1/mp.mpf(4))

# Compute the Hurwitz zeta function at s=3 for a=3/4
zeta2 = mp.zeta(3, 3/mp.mpf(4))

# Subtract the two results
result = zeta1 - zeta2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))