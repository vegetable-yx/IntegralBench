import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate trigonometric components
cos_1 = mp.cos(1)  # Compute cosine of 1 radian
sin_1 = mp.sin(1)  # Compute sine of 1 radian

# Calculate the polynomial combination of trigonometric values
trig_combination = 5*cos_1 - 3*sin_1

# Calculate the square root component
sqrt2 = mp.sqrt(2)  # Compute square root of 2

# Combine all components for final result
result = 2 * sqrt2 * trig_combination

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))