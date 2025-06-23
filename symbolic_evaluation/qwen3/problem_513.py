import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Directly assign the exact integer result as a mpmath float
result = mp.mpf(113)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))