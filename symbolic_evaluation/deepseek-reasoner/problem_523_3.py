import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations
result = mp.log(2)  # Compute natural logarithm of 2
print(mp.nstr(result, n=10))