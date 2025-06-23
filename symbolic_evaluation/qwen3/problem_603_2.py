import mpmath as mp
mp.dps = 15  # Set internal decimal precision
result = mp.mpf(4)  # Convert exact integer to mpmath floating-point
print(mp.nstr(result, n=10))  # Print result rounded to 10 decimal places