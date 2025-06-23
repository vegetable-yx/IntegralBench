import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the expression inside the logarithm: 2 + sqrt(5)
inner_log = 2 + sqrt5

# Compute the natural logarithm of (2 + sqrt(5))
log_val = mp.log(inner_log)

# Multiply by pi/4
result = (mp.pi / 4) * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))