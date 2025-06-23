import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π^2 using mpmath's pi constant
pi_squared = mp.pi ** 2

# Divide by 48 to get the final result
result = pi_squared / 48

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))