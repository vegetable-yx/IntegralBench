import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# The expression is 506 times pi
# Break into steps for clarity
multiplier = 506
pi_constant = mp.pi
result = multiplier * pi_constant

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))