import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute ln(2) - natural logarithm of 2
ln2 = mp.log(2)

# Compute (ln(2))^2
ln2_sq = ln2 ** 2

# Compute the first term: (π/2) * (ln(2))^2
term1 = (mp.pi / 2) * ln2_sq

# Define the complex argument (1 + i) for the polylogarithm
z = 1 + mp.j

# Compute the trilogarithm (Li_3) at (1 + i)
tri_log = mp.polylog(3, z)

# Extract the imaginary part of the trilogarithm result
imag_part = mp.im(tri_log)

# Compute the second term: 4 * imaginary part of Li_3(1+i)
term2 = 4 * imag_part

# Sum both terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))