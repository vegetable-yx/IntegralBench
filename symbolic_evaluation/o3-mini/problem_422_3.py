import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate 2 raised to the power of 4/3
base = mp.mpf(2)
exponent = mp.mpf(4)/3
power_result = mp.power(base, exponent)

# Divide the result by 4
denominator = mp.mpf(4)
result = power_result / denominator

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))