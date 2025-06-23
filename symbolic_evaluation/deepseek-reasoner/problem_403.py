import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 7! (factorial of 7) using gamma function
n = 8  # gamma(n) = (n-1)!
result = mp.gamma(n)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))