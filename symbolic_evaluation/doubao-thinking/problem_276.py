import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate 2 * pi
two_pi = 2 * mp.pi

# Calculate square root of (2 * pi)
sqrt_two_pi = mp.sqrt(two_pi)

# Calculate hyperbolic sine of 3
sinh_3 = mp.sinh(3)

# Multiply the two components
result = sqrt_two_pi * sinh_3

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))