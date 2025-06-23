import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places
result = mp.catalan  # Calculate Catalan's constant
print(mp.nstr(result, n=10))