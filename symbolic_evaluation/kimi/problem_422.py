import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute 2 raised to the power of 4/3
power_result = mp.power(2, mp.mpf(4)/3)

# Multiply the result by 1/4
result = power_result / 4

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))