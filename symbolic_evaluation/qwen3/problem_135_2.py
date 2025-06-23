import mpmath as mp
mp.dps = 15

# Calculate 3 * π
three_pi = 3 * mp.pi

# Divide by 4 to get the final result
result = three_pi / 4

print(mp.nstr(result, n=10))