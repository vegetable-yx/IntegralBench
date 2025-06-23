import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the constant denominator
denominator = 2019

# Compute the fraction inside the square root
pi_over_denominator = mp.pi / denominator

# Calculate the square root of the pi fraction
result = mp.sqrt(pi_over_denominator)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))