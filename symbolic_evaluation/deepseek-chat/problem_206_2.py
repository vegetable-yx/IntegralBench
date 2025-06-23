import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^(3/2) as pi * sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)
pi_power = mp.pi * sqrt_pi

# Calculate 2^(3/2) as 2 * sqrt(2)
sqrt_2 = mp.sqrt(2)
two_power = 2 * sqrt_2

# Compute the final result: (pi^(3/2)) / (2^(3/2))
result = pi_power / two_power

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))