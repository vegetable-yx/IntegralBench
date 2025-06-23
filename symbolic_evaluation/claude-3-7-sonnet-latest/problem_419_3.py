import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π to the power of 2
pi_squared = mp.pi ** 2

# Divide π² by 6 to obtain the result
result = pi_squared / 6

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))