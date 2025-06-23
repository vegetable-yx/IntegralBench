import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate components of the expression step by step
sqrt_2 = mp.sqrt(2)          # Compute square root of 2
one_plus_sqrt2 = 1 + sqrt_2  # Add 1 to sqrt(2)
log_term = mp.log(one_plus_sqrt2)  # Compute natural logarithm
result = mp.pi * log_term    # Multiply by pi

print(mp.nstr(result, n=10))