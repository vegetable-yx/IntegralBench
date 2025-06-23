import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations
result = mp.pi  # Assign mathematical constant π using mpmath's implementation
print(mp.nstr(result, n=10))