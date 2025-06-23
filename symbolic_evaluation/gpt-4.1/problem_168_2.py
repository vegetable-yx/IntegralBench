import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign known constants:
#   mp.pi - the mathematical constant π (pi)
#   mp.catalan - Catalan's constant (G)
pi_val = mp.pi
catalan_val = mp.catalan  # Catalan's constant G

# Compute the expression: π * G
result = pi_val * catalan_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))