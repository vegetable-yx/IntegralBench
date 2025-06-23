import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the result as 1 divided by 2
result = mp.mpf(1) / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))