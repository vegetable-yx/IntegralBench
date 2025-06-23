import mpmath as mp
mp.dps = 15

from mpmath import mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the numerator and denominator of the fraction inside the log
numerator = sqrt2 + 1
denominator = sqrt2 - 1

# Compute the fraction: (sqrt(2) + 1) / (sqrt(2) - 1)
fraction = numerator / denominator

# Calculate the natural logarithm of the fraction
log_term = mp.log(fraction)

# Compute the constant multiplier: 1/(2*sqrt(2))
constant = 1 / (2 * sqrt2)

# Multiply constant by the logarithm to get the final result
result = constant * log_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))