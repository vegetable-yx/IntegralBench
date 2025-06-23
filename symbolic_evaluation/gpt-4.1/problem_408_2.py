import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of (5/3)
log_part = mp.log(mp.mpf('5') / mp.mpf('3'))

# Calculate the fraction 3/5
fraction_part = mp.mpf('3') / mp.mpf('5')

# Compute the expression inside the parentheses: ln(5/3) + 3/5 - 1
inner_expr = log_part + fraction_part - mp.mpf('1')

# Multiply the inner expression by 1/8
result = inner_expr / mp.mpf('8')

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))