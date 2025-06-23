import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute necessary constants
sqrt2 = mp.sqrt(2)
sqrt3 = mp.sqrt(3)
three_quarter = 3**mp.mpf('0.25')  # 3^(1/4)
three_minus_quarter = 1 / three_quarter  # 3^(-1/4)
inv_sqrt3 = 1 / sqrt3  # 1/sqrt(3)

# Compute first fraction: (1 + sqrt2 * 3^(1/4) + sqrt3) / (1 - sqrt2 * 3^(1/4) + sqrt3)
num1 = 1 + sqrt2 * three_quarter + sqrt3
den1 = 1 - sqrt2 * three_quarter + sqrt3
frac1 = num1 / den1

# Compute second fraction: (1 - sqrt2 * 3^(-1/4) + 1/sqrt3) / (1 + sqrt2 * 3^(-1/4) + 1/sqrt3)
num2 = 1 - sqrt2 * three_minus_quarter + inv_sqrt3
den2 = 1 + sqrt2 * three_minus_quarter + inv_sqrt3
frac2 = num2 / den2

# Compute product of the two fractions
product = frac1 * frac2

# Take natural logarithm of the product
result = mp.log(product)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))