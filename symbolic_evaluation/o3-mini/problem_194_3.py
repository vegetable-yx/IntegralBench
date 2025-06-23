import mpmath as mp

# Set the decimal places of precision for internal calculations
mp.dps = 15

# Calculate the constant (sqrt(3) + 1) / 2
const1 = (mp.sqrt(3) + 1) / 2

# Calculate the constant (sqrt(3) - 1) / 2
const2 = (mp.sqrt(3) - 1) / 2

# Compute the natural logarithm of const1
log_val = mp.log(const1)

# Square the logarithm to get ln^2((sqrt(3)+1)/2)
log_sq = log_val ** 2

# Compute the dilogarithm (Li_2) of const2
dilog_val = mp.polylog(2, const2)

# Compute pi squared
pi_sq = mp.pi ** 2

# Combine the terms: pi_sq + 4 * log_sq - 8 * dilog_val
numerator = pi_sq + 4 * log_sq - 8 * dilog_val

# Divide by 32 to get the final result
result = numerator / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))