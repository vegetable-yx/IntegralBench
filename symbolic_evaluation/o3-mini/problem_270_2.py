import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi and square root of 3
pi = mp.pi
sqrt3 = mp.sqrt(3)

# Calculate each term separately

# Term 1: pi^3 / 96
term1 = pi**3 / 96

# Term 2: -pi^2 / 64
term2 = -pi**2 / 64

# Term 3: -pi * sqrt(3) / 192
term3 = -pi * sqrt3 / 192

# Term 4: (sqrt(3)/32) * ln((sqrt(3)+1)/2)
log_arg = (sqrt3 + 1) / 2
term4 = (sqrt3 / 32) * mp.log(log_arg)

# Term 5: (1/64) * [Li2((1-sqrt(3))/2) - Li2((sqrt(3)-1)/2)]
# Note: (1-sqrt(3))/2 and (sqrt(3)-1)/2 are negatives of each other
arg1 = (1 - sqrt3) / 2
arg2 = (sqrt3 - 1) / 2
dilog_diff = mp.polylog(2, arg1) - mp.polylog(2, arg2)
term5 = dilog_diff / 64

# Sum all terms
result = term1 + term2 + term3 + term4 + term5

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))