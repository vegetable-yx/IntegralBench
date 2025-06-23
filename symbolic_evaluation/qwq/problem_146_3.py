import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt2 = mp.sqrt(2)        # Compute square root of 2
pi_sqrt2 = mp.pi * sqrt2  # Multiply π by √2
numerator = 3 * pi_sqrt2  # Multiply by 3 for the numerator
result = numerator / 4    # Divide by 4 to get final result

print(mp.nstr(result, n=10))