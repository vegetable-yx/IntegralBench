import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the value of x for evaluation (chosen as 0.5 radians)
x_val = 0.5

# Compute sin(x) at the given x value
sin_x = mp.sin(x_val)

# Raise sin(x) to the 99th power
sin_x_power = sin_x**99

# Compute cos(101*x)
cos_101x = mp.cos(101 * x_val)

# Multiply cos(101*x) by sin(x)^99
numerator = cos_101x * sin_x_power

# Apply the coefficient and sign: - (numerator) / 101
result = -numerator / 101

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))