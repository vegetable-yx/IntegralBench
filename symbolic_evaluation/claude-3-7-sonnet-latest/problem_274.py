import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (example values - user should replace these as needed)
a = mp.mpf(1.0)  # Replace with actual value of a
b = mp.mpf(1.0)  # Replace with actual value of b

# Compute intermediate products
ab_product = a * b            # Calculate a*b
ab_half = ab_product / 2       # Calculate (a*b)/2
cosh_term = mp.cosh(ab_half)   # Compute cosh((a*b)/2)

# Compute a^3
a_cubed = a**3

# Compute final result: (a^3 / 4) * cosh((a*b)/2)
result = (a_cubed / 4) * cosh_term

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))