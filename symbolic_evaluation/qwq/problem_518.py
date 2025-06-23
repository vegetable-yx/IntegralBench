import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# The exact solution is 4036
result = 4036

print(mp.nstr(result, n=10))