import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant term: 10747/10
constant_term = mp.mpf(10747) / 10

# Calculate the logarithmic term: 6 * ln(2)
log_term = 6 * mp.log(2)

# Sum both terms to get final result
result = constant_term + log_term

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))