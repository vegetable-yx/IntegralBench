import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations
result = mp.pi  # Assign the constant π from mpmath
print(mp.nstr(result, n=10))