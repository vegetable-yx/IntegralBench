import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the argument for the sine function: 1 / sqrt(2)
sqrt2 = mp.sqrt(2)  # Calculate square root of 2
arg = 1 / sqrt2     # Compute argument: 1 / sqrt(2)

# Calculate sine of the argument
sin_val = mp.sin(arg)

# Compute constant factor: sqrt(2 * pi)
two_pi = 2 * mp.pi   # Multiply 2 by pi
sqrt_2pi = mp.sqrt(two_pi)  # Square root of (2 * pi)

# Multiply components to get final result
result = sqrt_2pi * sin_val

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))