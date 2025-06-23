import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the cosine of 1 radian
cos_1 = mp.cos(1)

# Multiply the results to get the final value
result = sqrt_pi * cos_1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))