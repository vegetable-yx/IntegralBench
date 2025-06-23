import mpmath as mp
mp.dps = 15

# Calculate pi using mpmath constant
pi_value = mp.pi

# Square the pi value
pi_squared = mp.power(pi_value, 2)

# Compute reciprocal of pi squared
result = mp.fdiv(1, pi_squared)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))