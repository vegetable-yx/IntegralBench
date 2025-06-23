import mpmath as mp
mp.dps = 15

# Calculate 3 times pi
three_pi = 3 * mp.pi

# Divide by 8 to get the final result
result = three_pi / 8

print(mp.nstr(result, n=10))