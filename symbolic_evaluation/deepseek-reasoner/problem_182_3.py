import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute square root of 5
sqrt5 = mp.sqrt(5)

# Compute the logarithm term ln(2 + sqrt(5))
log_term = mp.log(2 + sqrt5)

# Combine all components of the expression inside the parentheses
inner_expr = 1 - sqrt5 + 2 * log_term

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * inner_expr

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))