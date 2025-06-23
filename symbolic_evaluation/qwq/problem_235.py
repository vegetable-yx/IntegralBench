import mpmath as mp
mp.dps = 15  # Set internal decimal places for high precision calculations

# Calculate the numerator value
numerator = 16

# Get the precise value of π from mpmath
pi_value = mp.pi

# Compute the final result by dividing numerator by π
result = numerator / pi_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))