import mpmath as mp
mp.dps = 15

# Calculate pi divided by 2
result = mp.pi / 2

print(mp.nstr(result, n=10))