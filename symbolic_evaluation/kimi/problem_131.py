import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate the argument for the Bessel function
argument = 2 * mp.sqrt(2)

# Compute the order of the modified Bessel function
order = -mp.mpf(1)/4

# Calculate the modified Bessel function of the first kind
bessel_value = mp.besseli(order, argument)

# Multiply by the coefficient 8/3 with high precision
coefficient = mp.mpf(8)/3
result = coefficient * bessel_value

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))