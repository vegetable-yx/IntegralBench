import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi squared using mpmath's constant
pi_squared = mp.pi ** 2

# Convert result to 10 decimal places and print
print(mp.nstr(pi_squared, n=10))