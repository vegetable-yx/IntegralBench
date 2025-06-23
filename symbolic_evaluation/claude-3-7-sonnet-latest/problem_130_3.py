import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Step-by-step computation of π * √2 / 2
# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Multiply π by the square root of 2
pi_times_sqrt2 = mp.pi * sqrt_two

# Divide the result by 2 to obtain the final value
result = pi_times_sqrt2 / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))