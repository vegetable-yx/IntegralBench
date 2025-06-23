import mpmath as mp

mp.dps = 15  # Set internal decimal places for high precision

# Define constants: pi and Catalan's constant (G)
pi = mp.pi
catalan = mp.catalan  # Catalan's constant G

# Compute the expression: (1/12) * pi * G
product = pi * catalan
result = product / 12

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))