import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 5/3
log_term = mp.log(mp.mpf(5)/3)

# Calculate the constant fraction 2/5
fraction_term = mp.mpf(2)/5

# Compute the difference between logarithmic term and fraction
difference = log_term - fraction_term

# Final result scaled by 1/8
result = difference / 8

print(mp.nstr(result, n=10))