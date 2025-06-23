import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/4 using mpmath's pi constant
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 3 using mpmath's log function
ln_3 = mp.log(3)

# Sum the two components to get final result
result = pi_over_4 + ln_3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))