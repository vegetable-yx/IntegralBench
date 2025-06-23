import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_val = mp.pi
pi_squared = pi_val ** 2

# Divide by 32 to get final result
result = pi_squared / 32

# Print result with 10 decimal places
print(mp.nstr(result, n=10))