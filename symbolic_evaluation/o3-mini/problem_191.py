import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute frequently used constants and expressions
sqrt2 = mp.sqrt(2)           # Square root of 2
a = 1 + sqrt2                # (1 + sqrt(2))
log_a = mp.log(a)            # ln(1 + sqrt(2))
pi = mp.pi                   # Pi constant

# Compute the terms in the expression
# Term 1: 27 * pi^3
term1 = 27 * pi**3

# Term 2: -256 * pi * [ln(1+sqrt(2))]^2
term2 = -256 * pi * log_a**2

# Term 3: 512 * ln(1+sqrt(2))
term3 = 512 * log_a

# Term 4: 288 * [Li2(1-sqrt(2)) - Li2(1/(1+sqrt(2)))]
# Note: 1/(1+sqrt(2)) = sqrt(2) - 1
x1 = 1 - sqrt2               # (1 - sqrt(2))
x2 = sqrt2 - 1               # 1/(1+sqrt(2)) = sqrt(2) - 1
dilog_diff = mp.polylog(2, x1) - mp.polylog(2, x2)
term4 = 288 * dilog_diff

# Term 5: 128 * pi
term5 = 128 * pi

# Sum all terms and divide by 12288
total = term1 + term2 + term3 + term4 + term5
result = total / 12288

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))