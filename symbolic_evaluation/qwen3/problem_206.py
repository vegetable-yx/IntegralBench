import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of π
sqrt_pi = mp.sqrt(mp.pi)

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Compute the final result by dividing the two square roots
result = sqrt_pi / sqrt_two

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))