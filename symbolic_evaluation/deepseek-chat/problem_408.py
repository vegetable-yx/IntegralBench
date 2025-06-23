import mpmath as mp

# Set internal decimal places for intermediate calculations
mp.dps = 15

# Compute the fraction 5/3
fraction = mp.mpf('5') / mp.mpf('3')

# Calculate the natural logarithm of the fraction
log_term = mp.log(fraction)

# Compute the constant 2/5
constant = mp.mpf('2') / mp.mpf('5')

# Subtract the constant from the logarithm term
difference = log_term - constant

# Multiply by 1/8
result = difference / mp.mpf('8')

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))