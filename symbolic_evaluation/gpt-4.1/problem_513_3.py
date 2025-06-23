import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the endpoints for the intervals
x0 = mp.mpf(-4)  # Lower limit of the entire integral
x1 = mp.mpf(-1)  # First root of the polynomial
x2 = mp.mpf(0)   # Second root
x3 = mp.mpf(1)   # Third root
x4 = mp.mpf(4)   # Upper limit

# Compute antiderivative values at each endpoint for the two expressions:
# Expression 1 (for regions where |x^3-x| = -x^3+x): F1(x) = -x^4/4 + x^2/2
# Expression 2 (for regions where |x^3-x| = x^3-x): F2(x) = x^4/4 - x^2/2

# Interval [-4, -1]: use F1
F1_x1 = -x1**4 / 4 + x1**2 / 2
F1_x0 = -x0**4 / 4 + x0**2 / 2
part1 = F1_x1 - F1_x0

# Interval [-1, 0]: use F2
F2_x2 = x2**4 / 4 - x2**2 / 2
F2_x1 = x1**4 / 4 - x1**2 / 2
part2 = F2_x2 - F2_x1

# Interval [0, 1]: use F1
F1_x3 = -x3**4 / 4 + x3**2 / 2
F1_x2 = -x2**4 / 4 + x2**2 / 2
part3 = F1_x3 - F1_x2

# Interval [1, 4]: use F2
F2_x4 = x4**4 / 4 - x4**2 / 2
F2_x3 = x3**4 / 4 - x3**2 / 2
part4 = F2_x4 - F2_x3

# Sum all parts to get the total integral
result = part1 + part2 + part3 + part4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))