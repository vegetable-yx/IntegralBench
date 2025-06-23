import mpmath as mp
mp.dps = 15  # Set decimal places for internal precision
result = mp.pi  # Assign the constant π from mpmath
print(mp.nstr(result, n=10))  # Print result with 10 decimal places