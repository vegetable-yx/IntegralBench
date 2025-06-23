import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π/2 using mpmath's pi constant
pi_value = mp.pi
result = pi_value / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))