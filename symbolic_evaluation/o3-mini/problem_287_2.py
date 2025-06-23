import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute common constants
sqrt2 = mp.sqrt(2)
a = 1 + sqrt2  # (1 + sqrt(2))
b = sqrt2 - 1  # (sqrt(2) - 1), positive
c = 1 - sqrt2  # (1 - sqrt(2)), negative

# Compute ln(1 + sqrt(2))
ln_a = mp.log(a)

# Compute the first term: π * [ln(1+√2)]^4 / 64
term1 = (mp.pi * ln_a**4) / 64

# Compute Li2(1 - √2) and Li2(√2 - 1)
li2_c = mp.polylog(2, c)  # Li2(1 - sqrt(2))
li2_b = mp.polylog(2, b)  # Li2(sqrt(2) - 1)

# Compute the second term: - [ln(1+√2)]^2 / 8 * [Li2(1-√2) + Li2(√2-1)]
term2 = -(ln_a**2 / 8) * (li2_c + li2_b)

# Compute Li3(1 - √2) and Li3(√2 - 1)
li3_c = mp.polylog(3, c)  # Li3(1 - sqrt(2))
li3_b = mp.polylog(3, b)  # Li3(sqrt(2) - 1)

# Compute the third term: 1/4 * [Li3(1-√2) - Li3(√2-1)]
term3 = (1/4) * (li3_c - li3_b)

# Compute (√2 - 1)^2 and (1 - √2)^2 (they are equal numerically)
b_sq = (sqrt2 - 1)**2
c_sq = (1 - sqrt2)**2  # same as b_sq

# Compute Li3((√2 - 1)^2) and Li3((1 - √2)^2) (they are identical)
li3_b_sq = mp.polylog(3, b_sq)
li3_c_sq = mp.polylog(3, c_sq)  # same as li3_b_sq

# Compute the fourth term: 1/8 * [Li3((√2-1)^2) - Li3((1-√2)^2)] = 0
term4 = (1/8) * (li3_b_sq - li3_c_sq)  # exactly zero

# Sum all terms
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))