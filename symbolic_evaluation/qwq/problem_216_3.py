import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
pi_value = mp.pi
result = mp.sqrt(pi_value)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))