import mpmath as mp
# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the numerator
numerator = mp.pi

# Define denominator value
denominator = 2019

# Compute the fraction pi/2019
fraction = numerator / denominator

# Calculate square root of the fraction
result = mp.sqrt(fraction)

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))