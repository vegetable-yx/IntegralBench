import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi
pi_sqrt2 = mp.pi * sqrt2

# Multiply by 5
result = 5 * pi_sqrt2

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))