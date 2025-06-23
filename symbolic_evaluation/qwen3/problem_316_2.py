import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm and its square
ln2 = mp.log(2)
ln2_squared = ln2 ** 2

# Calculate π²/12 component
pi_squared = mp.pi ** 2
pi_squared_over_12 = pi_squared / 12

# Combine components for the expression inside the square root multiplier
inner_expression = ln2_squared - pi_squared_over_12

# Multiply by √2 for final result
result = mp.sqrt(2) * inner_expression

print(mp.nstr(result, n=10))