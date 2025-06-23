import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the cosine of 1 radian
cos1 = mp.cos(1)

# Multiply components: 2 * sqrt(pi) * cos(1)
result = 2 * sqrt_pi * cos1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))