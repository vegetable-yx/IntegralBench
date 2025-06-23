import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the natural logarithm of 2
log_two = mp.log(2)

# Negate the logarithm to get the final result
result = -log_two

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))