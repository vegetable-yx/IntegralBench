import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Evaluate the analytical expression: 1/2
# This is a simple rational number that can be computed exactly
numerator = mp.mpf(1)  # Define the numerator
denominator = mp.mpf(2)  # Define the denominator
result = numerator / denominator  # Compute the fraction

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))