import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute the analytical expression: 1/2
# This is a simple constant fraction
numerator = mp.mpf(1)  # Numerator of fraction
denominator = mp.mpf(2)  # Denominator of fraction
result = numerator / denominator  # Evaluate fraction

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))