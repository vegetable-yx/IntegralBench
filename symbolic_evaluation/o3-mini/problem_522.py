import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate the denominator
denominator = 2019

# Compute the fraction: pi divided by 2019
fraction = pi_val / denominator

# Compute the square root of the fraction
result = mp.sqrt(fraction)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))