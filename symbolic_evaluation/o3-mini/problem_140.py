import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Calculate I_0(2) - modified Bessel function of the first kind, order 0
I0 = mp.besseli(0, 2)

# Calculate I_1(2) - modified Bessel function of the first kind, order 1
I1 = mp.besseli(1, 2)

# Compute the expression inside the parentheses: 41*I1 - 17*I0
inner_expr = 41 * I1 - 17 * I0

# Multiply by 2: 2 * (41*I1 - 17*I0)
numerator = 2 * inner_expr

# Divide by 15 to get the final result
result = numerator / 15

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))