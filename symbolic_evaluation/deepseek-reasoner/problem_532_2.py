import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate pi squared using mpmath's constant
pi_value = mp.pi
pi_squared = pi_value ** 2

# Print result with exactly 10 decimal places
print(mp.nstr(pi_squared, n=10))