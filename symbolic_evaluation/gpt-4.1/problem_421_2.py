import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute sin(1) using mpmath
result = mp.sin(1)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))