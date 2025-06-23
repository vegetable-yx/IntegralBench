import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (user can modify this as needed)
a = mp.mpf(1)

# Calculate intermediate values
a_sq = a**2
arg = -a_sq / 4  # Common argument for hypergeometric functions

# Compute first hypergeometric function: _1F_2(1; 1/2, 1; -a^2/4)
hyp1 = mp.hyper([1], [mp.mpf('0.5'), 1], arg)

# Compute second hypergeometric function: _1F_2(1; 1, 3/2; -a^2/4)
hyp2 = mp.hyper([1], [1, mp.mpf('1.5')], arg)

# Combine terms according to the analytical expression
term1 = -mp.pi * hyp1
term2 = 2 * a * hyp2
combined = term1 + term2
result = combined / 4

# Print final result with exactly 10 decimal places
print(mp.nstr(result, n=10))