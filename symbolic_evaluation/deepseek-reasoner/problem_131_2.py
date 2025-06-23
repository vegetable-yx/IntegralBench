import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# The analytical expression is simply the constant π
result = mp.pi  # Print result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))