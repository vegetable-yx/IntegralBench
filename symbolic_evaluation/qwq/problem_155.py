import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = pi_value ** 3

# Divide by 16 to get the final result
result = pi_cubed / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))