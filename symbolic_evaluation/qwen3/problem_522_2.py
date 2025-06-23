import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the numerator (pi)
numerator = mp.pi

# Calculate the denominator
denominator = 2019

# Compute the fraction pi/2019
fraction = numerator / denominator

# Calculate the square root of the fraction
result = mp.sqrt(fraction)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))