import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first term: (ln(3) * pi) / (12 * sqrt(3))
ln3 = mp.ln(3)        # Natural logarithm of 3
pi = mp.pi             # Pi constant
sqrt3 = mp.sqrt(3)     # Square root of 3

numerator = ln3 * pi
denominator = 12 * sqrt3
first_term = numerator / denominator

# The integral term is known to be zero by symmetry
integral_value = 0
second_term = (1 / sqrt3) * integral_value

# Combine both terms
result = first_term + second_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))