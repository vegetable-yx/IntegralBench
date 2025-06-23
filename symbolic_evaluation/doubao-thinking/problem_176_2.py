import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = pi_value ** 3

# Divide by 24 to get final result
result = pi_cubed / 24

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))