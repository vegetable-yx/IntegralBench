import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Precompute commonly used constants
pi = mp.pi
sqrt3 = mp.sqrt(3)

# Term 1: π^3 / 96
term1 = pi**3 / 96

# Term 2: - (π * sqrt(3) / 64) * (8 - π^2)
term2 = - (pi * sqrt3 / 64) * (8 - pi**2)

# Term 3: (3 * sqrt(3) / 64) * ln( (3 + sqrt(3)) / (3 - sqrt(3)) )
log_arg3 = (3 + sqrt3) / (3 - sqrt3)
term3 = (3 * sqrt3 / 64) * mp.log(log_arg3)

# Term 4: (3 * π / 32) * ln( (sqrt(3) + 1) / 2 )
log_arg4 = (sqrt3 + 1) / 2
term4 = (3 * pi / 32) * mp.log(log_arg4)

# Term 5: - (3/16) * Li_2(1/2 - sqrt(3)/4)
arg5 = mp.mpf('0.5') - sqrt3 / 4
term5 = - (3 / 16) * mp.polylog(2, arg5)

# Term 6: (3/16) * Li_2(1/2 + sqrt(3)/4)
arg6 = mp.mpf('0.5') + sqrt3 / 4
term6 = (3 / 16) * mp.polylog(2, arg6)

# Sum all terms
result = term1 + term2 + term3 + term4 + term5 + term6

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))