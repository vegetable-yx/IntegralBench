import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the logarithm component: ln(5/3)
log_argument = mp.mpf(5)/3  # Compute the fraction 5/3 with high precision
log_value = mp.log(log_argument)  # Natural logarithm of 5/3

# Calculate the rational component: 2/5
rational_component = mp.mpf(2)/5  # Convert 2/5 to high-precision float

# Compute the difference between logarithmic and rational components
difference = log_value - rational_component

# Multiply by 1/8 to get the final result
result = difference * mp.mpf(1)/8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))