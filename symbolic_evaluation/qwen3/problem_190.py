import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant: 1 + sqrt(2)
x = mp.mpf(1) + mp.sqrt(2)

# Compute the natural logarithm of x
ln_x = mp.log(x)

# Compute the square and cube of the logarithm
ln_x_sq = ln_x ** 2
ln_x_cu = ln_x ** 3

# Calculate the first term: (pi/16) * (ln(1+sqrt(2)))^2
term1 = (mp.pi / 16) * ln_x_sq

# Calculate the second term: (pi/96) * (ln(1+sqrt(2)))^3
term2 = (mp.pi / 96) * ln_x_cu

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))