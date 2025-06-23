import mpmath as mp
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the golden ratio (1 + sqrt(5))/2
golden_ratio = (1 + sqrt5) / 2

# Calculate natural logarithm of the golden ratio
log_term = mp.log(golden_ratio)

# Multiply by 1/2*pi and the logarithmic term
result = (mp.pi / 2) * log_term

print(mp.nstr(result, n=10))