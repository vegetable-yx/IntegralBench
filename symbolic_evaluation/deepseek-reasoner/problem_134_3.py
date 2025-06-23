import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the square root of 2
sqrt_two = mp.sqrt(2)

# Divide pi by sqrt(2) to get the final result
result = pi_value / sqrt_two

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))