import mpmath as mp
mp.dps = 15

# Calculate 7! using gamma function (gamma(n) = (n-1)!)
result = mp.gamma(8)  # gamma(8) = 7! = 5040

print(mp.nstr(result, n=10))