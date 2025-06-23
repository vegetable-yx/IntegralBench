import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant term
constant_term = mp.mpf(2)

# Calculate pi divided by 2
pi_half = mp.pi / 2

# Subtract pi/2 from the constant
result = constant_term - pi_half

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))