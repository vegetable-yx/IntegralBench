import mpmath as mp

# Set internal decimal precision to 15 to ensure accurate computation
mp.dps = 15

# Calculate pi to the fourth power
pi_to_the_fourth = mp.pi ** 4

# Denominator is 120
denominator = 120

# Compute the result: pi^4 divided by 120
result = pi_to_the_fourth / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))