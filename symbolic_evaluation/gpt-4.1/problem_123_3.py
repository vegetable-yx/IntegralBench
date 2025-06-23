import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi using mpmath constant
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Divide by 32 to get the result
result = pi_cubed / 32

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))