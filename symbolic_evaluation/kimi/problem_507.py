import mpmath as mp
mp.dps = 15  # Direct assignment of constant value
result = 18

print(mp.nstr(result, n=10))