import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Precompute fundamental constants
sqrt2 = mp.sqrt(2)
pi = mp.pi
ln2 = mp.log(2)

# Compute ln(1 + sqrt(2))
ln_1p_sqrt2 = mp.log(1 + sqrt2)

# Calculate the logarithmic terms for the pi-multiplied part
ln_term1 = 8 * ln_1p_sqrt2**2
ln_term2 = -16 * ln2 * ln_1p_sqrt2
ln_term3 = 8 * ln2**2
ln_term4 = -pi**2

# Combine logarithmic terms and multiply by pi
log_terms_sum = ln_term1 + ln_term2 + ln_term3 + ln_term4
pi_multiplied = pi * log_terms_sum

# Compute arguments for the dilogarithm functions
dilog_arg1 = 1 - 1/sqrt2  # Positive argument ≈ 0.2929
dilog_arg2 = 1 - sqrt2     # Negative argument ≈ -0.4142

# Evaluate dilogarithms and their difference
dilog1 = mp.polylog(2, dilog_arg1)
dilog2 = mp.polylog(2, dilog_arg2)
dilog_diff = 32 * (dilog1 - dilog2)

# Combine all components and apply the 1/64 factor
total_inside = pi_multiplied + dilog_diff
result = total_inside / 64

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))