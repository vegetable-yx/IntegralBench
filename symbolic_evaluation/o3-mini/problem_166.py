import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the exact value of π/4 using mpmath constants
result = mp.pi / 4

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))