import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate common constants
sqrt2 = mp.sqrt(2)
inv_sqrt2 = 1 / sqrt2  # 1/sqrt(2)

# Compute the logarithmic term: ln(1 + sqrt(2))
ln_term = mp.log(1 + sqrt2)

# Compute the squared logarithm: [ln(1 + sqrt(2))]^2
ln_sq = ln_term ** 2

# Compute the dilogarithm terms
dilog1 = mp.polylog(2, -inv_sqrt2)           # Li_2(-1/sqrt(2))
dilog2 = mp.polylog(2, 1 - inv_sqrt2)        # Li_2(1 - 1/sqrt(2))

# Compute the trilogarithm terms
trilog1 = mp.polylog(3, 1 - sqrt2)           # Li_3(1 - sqrt(2))
trilog2 = mp.polylog(3, sqrt2 - 1)           # Li_3(sqrt(2) - 1)

# Construct the inner expression inside the square brackets:
# 16*ln_sq + 8*dilog1 - 8*dilog2 + 3*pi^2
inner_expr = 16 * ln_sq + 8 * dilog1 - 8 * dilog2 + 3 * mp.pi**2

# Multiply inner expression by -pi: -pi * inner_expr
partA = -mp.pi * inner_expr

# Compute the trilogarithm difference: 16 * [trilog1 - trilog2]
partB = 16 * (trilog1 - trilog2)

# Sum parts A and B, then divide by 96 to get the final result
result = (partA + partB) / 96

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))