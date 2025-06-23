import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate base 2 raised to the power of 4/3
exponent = mp.mpf(4)/3
power_result = mp.power(2, exponent)

# Multiply the result by 1/4
result = power_result * mp.mpf(1)/4

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))