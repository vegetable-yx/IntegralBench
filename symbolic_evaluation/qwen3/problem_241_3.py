import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Compute reciprocal of pi squared
result = mp.fdiv(1, pi_squared)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))