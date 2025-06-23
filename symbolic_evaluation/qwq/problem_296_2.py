import mpmath as mp
mp.dps = 15  # Set decimal precision for all calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π squared
pi_squared = mp.power(pi_value, 2)

# Compute π to the fourth power by squaring π squared
pi_fourth = mp.power(pi_squared, 2)

# Calculate the final result by dividing π^4 by 96
result = pi_fourth / 96

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))