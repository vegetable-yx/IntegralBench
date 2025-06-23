import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate intermediate constants
sqrt2 = mp.sqrt(2)  # Square root of 2
a = 1 + sqrt2       # 1 + sqrt(2)

# Compute the logarithm and its square
ln_val = mp.log(a)   # Natural logarithm of (1 + sqrt(2))
ln_sq = ln_val**2    # Squared logarithm term

# Calculate the argument for the dilogarithm
b = 1 / a            # Reciprocal: 1/(1 + sqrt(2))

# Compute the dilogarithm function
dilog_term = mp.polylog(2, b)  # Li_2(1/(1+sqrt(2)))

# Construct the expression components
pi_sq = mp.pi**2               # π squared
term1 = pi_sq                  # π² term
term2 = 4 * ln_sq              # 4 * [ln(1+sqrt(2))]^2
term3 = -8 * dilog_term        # -8 * Li_2(1/(1+sqrt(2)))

# Combine terms and divide by 8
numerator = term1 + term2 + term3
result = numerator / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))