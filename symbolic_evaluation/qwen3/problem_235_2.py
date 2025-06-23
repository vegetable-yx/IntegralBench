import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Define the numerator
numerator = 8

# Get the value of pi using mpmath's constant
pi_value = mp.pi

# Compute the result: 8 divided by pi
result = numerator / pi_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))