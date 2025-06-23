import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define constant k = 1/4
k = 0.25
k2 = k**2  # k squared = 0.0625

# First term: (1/16) * pi * arcsin(k)
term1 = (mp.pi / 16) * mp.asin(k)

# Compute I1: integral of theta * cos(theta) / sqrt(1 - k^2 sin^2(theta)) from 0 to pi/2
# Using integration by parts and series expansion result:
# I1 = (pi/(2k)) * asin(k) - (1/(2k)) * [Li_2(k) - Li_2(-k)]
I1_part1 = (mp.pi / (2 * k)) * mp.asin(k)
I1_part2 = (mp.polylog(2, k) - mp.polylog(2, -k)) / (2 * k)
I1 = I1_part1 - I1_part2

# Compute I2: integral of sin(theta) * cos^2(theta) / sqrt(1 - k^2 sin^2(theta)) from 0 to pi/2
# Using hypergeometric function representation:
# I2 = (1/3) * hyp2f1(1/2, 1, 5/2, k^2)
I2 = mp.hyp2f1(0.5, 1, 2.5, k2) / 3

# Combine integrals: bracket = I1 + I2
bracket = I1 + I2

# Final result: term1 - (1/4) * bracket
result = term1 - (1/4) * bracket

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))