import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi raised to the power of 3/2
pi_power = mp.power(mp.pi, 1.5)

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Divide pi^(3/2) by sqrt(2)
result = pi_power / sqrt_two

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))