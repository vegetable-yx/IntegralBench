import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute digamma function values
digamma_3 = mp.digamma(3)          # ψ(3)
digamma_3over2 = mp.digamma(mp.mpf(3)/2)  # ψ(3/2)

# Compute trigamma function values
trigamma_3over2 = mp.polygamma(1, mp.mpf(3)/2)  # ψ₁(3/2)
trigamma_3 = mp.polygamma(1, 3)    # ψ₁(3)

# Calculate the expression inside the square brackets
bracket = 2*ln2 + digamma_3 - digamma_3over2
bracket_sq = bracket**2            # Square of the bracket

# Compute 2 times ln²(2)
two_ln2_sq = 2 * (ln2**2)

# Combine terms for the inner expression
inner_expr = bracket_sq - two_ln2_sq - trigamma_3over2 + trigamma_3

# Multiply by π and divide by 2048
result = (mp.pi / 2048) * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))