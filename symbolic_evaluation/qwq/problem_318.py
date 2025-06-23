import mpmath as mp
mp.dps = 15

# Compute the first term: sqrt(3)/2
sqrt3_over_2 = mp.sqrt(3) / 2

# Compute the complete elliptic integral of the second kind at 1/2
elliptic_term = mp.ellipe(0.5)

# Compute the natural logarithm of 2
log_term = mp.log(2)

# Combine all terms for final result
result = sqrt3_over_2 * elliptic_term + log_term

print(mp.nstr(result, n=10))