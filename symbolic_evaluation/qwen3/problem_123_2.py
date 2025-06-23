import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the value of pi
pi_value = mp.pi

# Compute pi squared
pi_squared = pi_value ** 2

# Divide by 4 to obtain the final result
result = pi_squared / 4

# Output the result with 10 decimal places
print(mp.nstr(result, n=10))