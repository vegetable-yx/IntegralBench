import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the value of π
pi_val = mp.pi

# Compute the denominator (2019)
denominator = 2019

# Calculate the fraction: π / 2019
fraction = pi_val / denominator

# Compute the square root of the fraction
result = mp.sqrt(fraction)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))