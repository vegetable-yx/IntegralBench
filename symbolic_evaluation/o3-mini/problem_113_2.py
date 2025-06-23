import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Calculate the hypergeometric function 3F2([1/4, 1/2, 3/4]; [5/4, 1]; 1)
hyp_val = mp.hyper3f2(
    [mp.mpf(1)/4, mp.mpf(1)/2, mp.mpf(3)/4],
    [mp.mpf(5)/4, mp.mpf(1)],
    1
)

# Calculate the expression inside the braces: 8 * hyp_val - gamma_14^2
inner_braces = 8 * hyp_val - gamma_14**2

# Calculate the denominator: 16 * sqrt(2)
denominator = 16 * mp.sqrt(2)

# Combine all parts: (gamma_14^2 * inner_braces) / denominator
result = (gamma_14**2 * inner_braces) / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))