import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate hyperbolic sine of 3
sinh_3 = mp.sinh(3)

# Multiply by pi to get final result
result = mp.pi * sinh_3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))