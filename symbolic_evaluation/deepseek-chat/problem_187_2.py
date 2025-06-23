import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(120)
sqrt120 = mp.sqrt(120)

# Calculate the expression inside the second square root: 240 + 22*sqrt(120)
inner_radical = 240 + 22 * sqrt120

# Compute the square root of the inner radical expression
sqrt_inner = mp.sqrt(inner_radical)

# Compute the numerator: 11 + sqrt(120) + sqrt_inner
numerator = 11 + sqrt120 + sqrt_inner

# Divide by 2 to get the argument of the logarithm
log_arg = numerator / 2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Multiply by pi/8 to get the final result
result = (mp.pi / 8) * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))