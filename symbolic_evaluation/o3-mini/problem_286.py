import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute frequently used constant: sqrt(2)
sqrt2 = mp.sqrt(2)

# Intermediate values
a = 1 + sqrt2                # 1 + sqrt(2)
b = (3 + 2*sqrt2) / 2        # (3 + 2*sqrt(2))/2
c = (sqrt2 - 1) / 2          # (sqrt(2) - 1)/2
d = 1 - 1/sqrt2              # 1 - 1/sqrt(2)

# Compute logarithms
log_a = mp.log(a)            # ln(1 + sqrt(2))
log_b = mp.log(b)            # ln((3 + 2*sqrt(2))/2)

# Compute terms
term1 = (mp.pi / 16) * log_a**2
term2 = (1/8) * log_a * log_b
term3 = (-1/4) * mp.polylog(2, c)
term4 = (1/4) * mp.polylog(2, d)

# Sum all terms
result = term1 + term2 + term3 + term4

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))