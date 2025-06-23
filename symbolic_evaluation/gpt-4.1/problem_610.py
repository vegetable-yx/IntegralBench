import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the exact constant value 1
result = mp.mpf(1)

# Print the result to exactly 10 decimal places using mp.nstr
print(mp.nstr(result, n=10))