import mpmath as mp
mp.dps = 15

# Calculate 1 minus the Euler-Mascheroni constant
gamma = mp.euler
result = 1 - gamma

print(mp.nstr(result, n=10))