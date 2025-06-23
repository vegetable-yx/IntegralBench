import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2 raised to the 4/3 power
base = mp.mpf(2)
exponent = mp.mpf(4)/3
power_result = base ** exponent

# Divide the result by 4
result = power_result / 4

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))