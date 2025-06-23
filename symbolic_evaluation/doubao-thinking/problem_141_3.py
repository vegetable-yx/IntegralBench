import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations
result = mp.mpf(1)  # Directly assign the analytical solution
print(mp.nstr(result, n=10))  # Print result with 10 decimal places