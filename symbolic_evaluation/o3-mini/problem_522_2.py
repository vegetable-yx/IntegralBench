import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the square root of 2019
sqrt_2019 = mp.sqrt(2019)

# Compute the final result: sqrt(pi) / sqrt(2019)
result = sqrt_pi / sqrt_2019

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))