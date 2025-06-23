import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the rational number component
rational_part = mp.mpf('10747') / mp.mpf('10')

# Calculate the logarithmic component
log_term = 6 * mp.log(2)

# Sum both components for final result
result = rational_part + log_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))