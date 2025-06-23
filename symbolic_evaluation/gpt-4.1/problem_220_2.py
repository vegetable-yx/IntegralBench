import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute the square root of 2
sqrt_2 = mp.sqrt(2)

# Compute the hypergeometric function 2F1(2, 1/2; 1; -1)
hyp_value = mp.hyp2f1(2, 0.5, 1, -1)

# Calculate the expression inside the brackets: sqrt(2) - hyp2f1(...)
inner_expr = sqrt_2 - hyp_value

# Multiply by pi
result = mp.pi * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))