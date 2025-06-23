import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Divide by 4 to get final result
result = sqrt_pi / 4

# Print result with 10 decimal places
print(mp.nstr(result, n=10))