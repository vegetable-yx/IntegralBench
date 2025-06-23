import mpmath as mp
mp.dps = 15

# Compute the integral result using analytical solution pi*sqrt(2)
result = mp.pi * mp.sqrt(2)

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))