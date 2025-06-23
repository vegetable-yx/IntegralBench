import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression (5*sqrt(2)*pi)/8
sqrt2 = mp.sqrt(2)        # Compute square root of 2
five_sqrt2 = 5 * sqrt2    # Multiply by 5
numerator = five_sqrt2 * mp.pi  # Multiply by pi
result = numerator / 8    # Divide by 8 to get final result

print(mp.nstr(result, n=10))