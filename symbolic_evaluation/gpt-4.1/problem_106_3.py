import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the constant π using mpmath
pi_value = mp.pi

# Evaluate the expression π/2
result = pi_value / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))