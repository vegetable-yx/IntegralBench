import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply pi by sqrt(2)
pi_times_sqrt2 = mp.pi * sqrt2

# Divide by 2 to get the final result
result = pi_times_sqrt2 / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))