import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b - USER MUST SET THESE VALUES
a = mp.mpf(1.0)  # Example value; replace with desired input
b = mp.mpf(1.0)  # Example value; replace with desired input

# Compute common argument: (a^2 * b^2)/4
arg = (a**2 * b**2) / 4

# Compute first hypergeometric term: _1F_2(1; 1.5, 2.5; arg)
hyp1 = mp.hyper([1], [mp.mpf('1.5'), mp.mpf('2.5')], arg)

# First part: (a^3 / 3) * hypergeometric result
term1 = (a**3 / 3) * hyp1

# Compute second hypergeometric term: _1F_2(2; 2.5, 3.5; arg)
hyp2 = mp.hyper([2], [mp.mpf('2.5'), mp.mpf('3.5')], arg)

# Second part: (a^3 * b^2 / 6) * hypergeometric result
term2 = (a**3 * b**2 / 6) * hyp2

# Sum both terms for final result
result = term1 + term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))