import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute ln(1 + sqrt(2))
log_term = mp.log(1 + mp.sqrt(2))

# Square the logarithmic term
log_squared = log_term ** 2

# Compute pi squared divided by 24
pi_squared_over_24 = (mp.pi ** 2) / 24

# Calculate the difference between squared log term and pi^2/24
difference = log_squared - pi_squared_over_24

# Multiply by pi/128 to get the final result
result = (mp.pi / 128) * difference

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))