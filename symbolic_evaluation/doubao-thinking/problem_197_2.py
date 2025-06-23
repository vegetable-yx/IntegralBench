import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the simple fraction 1/4 using exact arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(4)
result = numerator / denominator

# Output the result with 10 decimal place precision
print(mp.nstr(result, n=10))