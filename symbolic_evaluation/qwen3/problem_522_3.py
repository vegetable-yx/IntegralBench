import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate the denominator
denominator = 2019

# Compute the constant pi using mpmath's implementation
pi_value = mp.pi

# Calculate the fraction inside the square root
fraction = pi_value / denominator

# Compute the square root of the fraction
result = mp.sqrt(fraction)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))