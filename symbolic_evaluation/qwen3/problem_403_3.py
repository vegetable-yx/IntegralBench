import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate 7! using gamma function (gamma(n) = (n-1)!)
result = mp.gamma(8)

# Print the result with 10 decimal places (will show as integer with .0)
print(mp.nstr(result, n=10))