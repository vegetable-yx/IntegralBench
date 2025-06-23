import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the numerator: pi
numerator = mp.pi

# Denominator is the constant 2019
denominator = 2019

# Calculate the fraction: pi / 2019
fraction = numerator / denominator

# Take the square root of the fraction
result = mp.sqrt(fraction)

# Print the result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))