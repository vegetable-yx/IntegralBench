import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute digamma function at 0.125
psi_0125 = mp.digamma(0.125)

# Compute digamma function at 0.625
psi_0625 = mp.digamma(0.625)

# Calculate the difference between the two digamma values
diff = psi_0125 - psi_0625

# Multiply the difference by pi
result = mp.pi * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))