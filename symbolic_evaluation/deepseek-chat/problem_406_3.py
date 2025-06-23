import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for arcsine: (sqrt(3) - 1) / 2
sqrt_val = mp.sqrt(3)  # Compute square root of 3
numerator = sqrt_val - 1  # Compute numerator: sqrt(3) - 1
arg = numerator / 2  # Divide by 2 to get the argument

# Compute the arcsine of the argument
asin_val = mp.asin(arg)  # Use mp.asin for inverse sine

# Multiply by 2 to get the final result
result = 2 * asin_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))