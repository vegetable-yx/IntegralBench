import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the parameter a = 0.25
a = mp.mpf('0.25')

# Calculate the dilogarithm terms for positive and negative arguments
dilog_positive = mp.polylog(2, a)
dilog_negative = mp.polylog(2, -a)

# Compute the final result using the dilogarithm difference
result = (dilog_positive - dilog_negative) / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))