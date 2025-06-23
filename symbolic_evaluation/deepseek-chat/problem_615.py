import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the two components: 5√2
a = 5 * sqrt2

# Calculate the two bases: (5√2 + 7) and (5√2 - 7)
base1 = a + 7
base2 = a - 7

# Exponent for the expression: 4/3
exponent = mp.mpf(4)/3

# Raise each base to the power of 4/3
term1 = base1 ** exponent
term2 = base2 ** exponent

# Compute the difference: (5√2 + 7)^(4/3) - (5√2 - 7)^(4/3)
diff = term1 - term2

# Multiply by 3/4 to get the final result
result = (mp.mpf(3)/4) * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))