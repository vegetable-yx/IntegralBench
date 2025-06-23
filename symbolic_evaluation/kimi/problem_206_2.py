import mpmath as mp
mp.dps = 15

# Calculate the square root of pi
pi_value = mp.pi
result = mp.sqrt(pi_value)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))