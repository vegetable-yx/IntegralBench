import mpmath as mp
mp.dps = 15

# Compute 7! using gamma function (gamma(8) = 7!)
result = mp.gamma(8)

print(mp.nstr(result, n=10))