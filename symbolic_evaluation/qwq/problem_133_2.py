import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Divide pi by sqrt(2) to get the result
result = pi_val / sqrt2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))