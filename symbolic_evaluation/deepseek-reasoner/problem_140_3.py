import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Direct assignment of the constant result
result = mp.mpf(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))