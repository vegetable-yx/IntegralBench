import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate components of the expression
sqrt2 = mp.sqrt(2)          # Compute square root of 2
sin1 = mp.sin(1)            # Compute sine of 1 radian
cos1 = mp.cos(1)            # Compute cosine of 1 radian

# Calculate the trigonometric difference
trig_diff = sin1 - cos1     # Compute sin(1) - cos(1)

# Combine all components for final result
result = 2 * sqrt2 * trig_diff  # Multiply by 2*sqrt(2)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))