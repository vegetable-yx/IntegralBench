import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_term = mp.pi

# Cube the pi term
pi_cubed = pi_term ** 3

# Calculate denominator
denominator = 32

# Compute the final result
result = pi_cubed / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))