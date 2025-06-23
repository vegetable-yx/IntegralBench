import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define the natural logarithm of 2
ln2 = mp.log(2)

# Compute 4 * (ln(2))^2
four_ln2_squared = 4 * ln2**2

# Compute trigamma function at 1/2 (which is polygamma of order 1 at 0.5)
trigamma_half = mp.polygamma(1, 0.5)

# Compute trigamma function at 1 (which is polygamma of order 1 at 1)
trigamma_one = mp.polygamma(1, 1)

# Combine the inner expression: 4*(ln2)^2 + trigamma(1/2) - trigamma(1)
inner_expr = four_ln2_squared + trigamma_half - trigamma_one

# Multiply by -π/8
result = - (mp.pi / 8) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))