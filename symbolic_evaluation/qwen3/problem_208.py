import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π raised to the 5th power
pi_power5 = pi_value ** 5

# Divide π^5 by 810 to get the final result
result = pi_power5 / 810

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))