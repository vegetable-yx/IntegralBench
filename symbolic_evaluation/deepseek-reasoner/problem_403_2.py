import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 7! using gamma function (gamma(n) = (n-1)!)
result = mp.gamma(8)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))