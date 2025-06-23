import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations
result = mp.mpf(1)  # Direct assignment of analytical solution
print(mp.nstr(result, n=10))