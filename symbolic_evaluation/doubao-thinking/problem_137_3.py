import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places
result = mp.mpf(2)  # Assign the exact integer 2 as a mpmath floating-point number
print(mp.nstr(result, n=10))  # Print result formatted to 10 decimal places