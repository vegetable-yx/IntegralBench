import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Convert the constant 821.7 to an mpmath float for exact representation
constant = mp.mpf('821.7')

# Compute the natural logarithm of 2 using mp.log
ln2 = mp.log(2)

# Multiply the logarithm by 6
log_term = 6 * ln2

# Add the constant and the logarithmic term
result = constant + log_term

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))