import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the constant term
constant = mp.mpf(2)

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi/2 division
pi_over_2 = pi_value / 2

# Perform final subtraction
result = constant - pi_over_2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))