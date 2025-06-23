import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate individual components
sin_2 = mp.sin(2)        # Compute sin(2)
cos_2 = mp.cos(2)        # Compute cos(2)
term1 = sin_2 / 2        # Calculate sin(2)/2
difference = term1 - cos_2  # Compute (sin(2)/2 - cos(2))

# Combine components with constants
sqrt2 = mp.sqrt(2)       # Calculate square root of 2
numerator = sqrt2 * difference  # Multiply sqrt(2) with the difference
result = numerator / mp.pi      # Divide by pi to get final result

print(mp.nstr(result, n=10))