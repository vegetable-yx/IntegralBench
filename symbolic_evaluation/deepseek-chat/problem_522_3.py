import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate pi (using mpmath's constant)
pi_val = mp.pi

# Compute the fraction pi divided by 2019
fraction = pi_val / 2019

# Take the square root of the fraction
result = mp.sqrt(fraction)

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))