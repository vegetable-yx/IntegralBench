import mpmath as mp

# Set internal precision to 15 decimal places for accuracy
mp.dps = 15

# Compute the first hypergeometric function: _3F_2(1/2, 1/2, 1/2; 3/2, 3/2; 1/16)
hyper1 = mp.hyper([0.5, 0.5, 0.5], [1.5, 1.5], 1/16)

# Compute the second hypergeometric function: _3F_2(1/2, 1/2, 1; 3/2, 3/2; 1/16)
hyper2 = mp.hyper([0.5, 0.5, 1], [1.5, 1.5], 1/16)

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Calculate the expression inside the brackets: 16 * hyper1 - 8 * ln2 * hyper2
bracket_expr = 16 * hyper1 - 8 * ln2 * hyper2

# Multiply by 1/32 to get the final result
result = bracket_expr / 32

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))