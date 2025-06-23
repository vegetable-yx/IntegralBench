import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate 5/3 fraction with high precision
fraction = mp.mpf(5)/mp.mpf(3)

# Compute natural logarithm of the fraction
log_term = mp.log(fraction)

# Calculate 2/5 with high precision
constant_term = mp.mpf(2)/mp.mpf(5)

# Combine terms and divide by 8
result = (log_term - constant_term) / mp.mpf(8)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))