import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate 2 raised to the power of 4/3
base = mp.mpf(2)
exponent = mp.mpf(4)/mp.mpf(3)
power_result = mp.power(base, exponent)

# Divide the result by 4
denominator = mp.mpf(4)
result = power_result / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))