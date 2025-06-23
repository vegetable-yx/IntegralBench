import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute the logarithm term: ln(sqrt(2) + 1)
log_term = mp.log(sqrt2 + 1)

# Compute the integral of sec^3(theta) from 0 to pi/4 analytically
# The antiderivative is (1/2)(sec(theta)tan(theta) + ln|sec(theta) + tan(theta)|)
# Evaluate at upper limit (pi/4):
#   sec(pi/4) = sqrt(2), tan(pi/4) = 1
#   term_upper = sqrt(2)*1 + ln(sqrt(2) + 1) = sqrt2 + log_term
# Evaluate at lower limit (0):
#   sec(0) = 1, tan(0) = 0 -> term_lower = 0
# Integral = (1/2) * (term_upper - term_lower) = (sqrt2 + log_term)/2
integral_value = (sqrt2 + log_term) / 2

# Compute the entire expression:
#   result = -1 + sqrt2 * log_term + sqrt2 * integral_value
result = -1 + sqrt2 * log_term + sqrt2 * integral_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))