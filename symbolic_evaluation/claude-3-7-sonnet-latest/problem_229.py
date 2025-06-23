import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Compute pi to the power of 3
pi_cubed = mp.pi ** 3

# Divide by 96 to get the result
result = pi_cubed / 96

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))