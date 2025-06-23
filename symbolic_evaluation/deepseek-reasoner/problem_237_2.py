import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate components separately
sqrt2 = mp.sqrt(2)  # Compute √2
cos1 = mp.cos(1)    # Compute cosine of 1 radian

# Multiply components in steps
term1 = 2 * sqrt2    # 2√2
term2 = term1 * mp.pi  # Multiply by π
result = term2 * cos1  # Final multiplication with cos(1)

print(mp.nstr(result, n=10))