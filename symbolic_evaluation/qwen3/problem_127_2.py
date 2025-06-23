import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Gamma(3/4)
gamma_34 = mp.gamma(3/4)

# Square the Gamma(3/4) value
gamma_squared = gamma_34 ** 2

# Calculate the numerator = sqrt(2) * pi
numerator = mp.sqrt(2) * mp.pi

# Compute the final result by dividing numerator by gamma_squared
result = numerator / gamma_squared

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))