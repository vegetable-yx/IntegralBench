import mpmath as mp
mp.dps = 15  # Set internal decimal precision to 15 digits

# Calculate the rational number component
rational_part = mp.mpf(10747)/10  # Compute 10747/10 with high precision

# Calculate the logarithmic component
log_term = mp.log(2)  # Natural logarithm of 2
log_part = 6 * log_term  # Multiply by coefficient 6

# Combine both components for final result
result = rational_part + log_part

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))