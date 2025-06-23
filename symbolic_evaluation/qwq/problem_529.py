import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations
result = -mp.pi  # Compute negative value of pi
print(mp.nstr(result, n=10))  # Print result with 10 decimal places