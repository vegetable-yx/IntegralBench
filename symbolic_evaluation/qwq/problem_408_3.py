import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the natural logarithm term ln(5/3)
log_arg = mp.mpf(5)/mp.mpf(3)  # Compute 5/3 as a mpmath float
log_term = mp.log(log_arg)     # Compute ln(5/3)

# Calculate the constant term 2/5
constant_term = mp.mpf(2)/mp.mpf(5)  # Compute 2/5

# Combine terms and multiply by 1/8
result = (log_term - constant_term) * mp.mpf(1)/mp.mpf(8)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))