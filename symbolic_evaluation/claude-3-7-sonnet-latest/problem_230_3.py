import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute common constants
pi = mp.pi
ln2 = mp.log(2)

# Calculate each term separately
term1 = mp.power(pi, 3) / 96
term2 = (pi / 2) * mp.power(ln2, 2)
term3 = (mp.power(pi, 2) / 6) * ln2
term4 = (1/3) * mp.power(ln2, 3)
term5 = (1/4) * mp.zeta(3)

# Combine terms according to the expression
result = term1 - term2 + term3 - term4 - term5

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))