import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant multiplier
multiplier = mp.mpf(3)

# Access the constant pi from mpmath
pi_constant = mp.pi

# Multiply 3 by pi
result = multiplier * pi_constant

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))