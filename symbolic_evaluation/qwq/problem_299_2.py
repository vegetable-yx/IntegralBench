import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Beta(1/4, 1/2)
beta_term = mp.beta(mp.mpf(1)/4, mp.mpf(1)/2)

# Calculate natural logarithm of 2
ln2 = mp.ln(2)

# Calculate pi/2
pi_half = mp.pi / 2

# Calculate the sum (ln2 + pi/2)
log_pi_sum = ln2 + pi_half

# Multiply Beta term with logarithmic sum
beta_log_product = beta_term * log_pi_sum

# Note: I_2b component is undefined in the original expression
# This code will raise a NameError since I_2b is not defined
result = 2 * (beta_log_product + I_2b)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))