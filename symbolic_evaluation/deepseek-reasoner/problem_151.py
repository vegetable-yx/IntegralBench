import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath constant
pi_value = mp.pi

# Square the value of pi
pi_squared = mp.power(pi_value, 2)

# Print result with exactly 10 decimal places
print(mp.nstr(pi_squared, n=10))