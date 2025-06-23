import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define numerator and denominator
numerator = 2023
denominator = 2022

# Calculate the fraction: 2023 / 2022
fraction = mp.mpf(numerator) / mp.mpf(denominator)

# Apply the negative sign to get the result
result = -fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))