import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# The analytical answer is the constant 3
result = mp.mpf(3)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))