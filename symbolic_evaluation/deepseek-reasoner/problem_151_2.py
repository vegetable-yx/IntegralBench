import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi squared using mpmath's constant for pi
pi_value = mp.pi
pi_squared = pi_value ** 2

# Print the result with exactly 10 decimal places
print(mp.nstr(pi_squared, n=10))