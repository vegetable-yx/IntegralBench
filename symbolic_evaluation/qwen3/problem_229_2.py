import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi = mp.pi

# Compute pi raised to the fourth power
pi_power4 = mp.power(pi, 4)

# Divide by 1920 to get the final result
result = pi_power4 / 1920

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))