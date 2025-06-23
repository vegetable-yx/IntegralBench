import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate square root of 24
sqrt_24 = mp.sqrt(24)

# Compute the numerator coefficient (5 + sqrt(24))
numerator_coeff = 5 + sqrt_24

# Calculate pi squared
pi_squared = mp.pi**2

# Multiply numerator components
product = numerator_coeff * pi_squared

# Final division by 32
result = product / 32

# Print result with 10 decimal places
print(mp.nstr(result, n=10))