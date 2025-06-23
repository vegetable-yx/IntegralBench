import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the mathematical constant π
pi_value = mp.pi

# Evaluate the expression π/4
result = pi_value / 4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))