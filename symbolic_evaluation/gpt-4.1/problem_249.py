import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute (sqrt(5)/2)
half_sqrt5 = sqrt5 / 2

# Subtract 1: (sqrt(5)/2 - 1)
expression = half_sqrt5 - 1

# Multiply by pi
result = mp.pi * expression

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))