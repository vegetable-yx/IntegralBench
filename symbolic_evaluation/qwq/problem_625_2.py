import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply π by sqrt(2)
pi_times_sqrt2 = mp.fmul(pi_value, sqrt_2)

# Divide the result by 4 to get final value
result = mp.fdiv(pi_times_sqrt2, 4)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))