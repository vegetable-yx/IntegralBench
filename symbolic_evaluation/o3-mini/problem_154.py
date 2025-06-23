import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute constant: 1 + sqrt(2)
a = 1 + mp.sqrt(2)

# Compute (1 + sqrt(2))^2
a_sq = a**2

# Compute reciprocal: 1 / (1 + sqrt(2))^2
rec = 1 / a_sq

# Compute ln(1 + sqrt(2))
ln_a = mp.log(a)

# Compute [ln(1 + sqrt(2))]^2
ln_a_sq = ln_a**2

# First term: (pi/8) * [ln(1 + sqrt(2))]^2
term1 = (mp.pi / 8) * ln_a_sq

# Compute arguments for dilogarithms
arg1 = 1 - rec   # 1 - 1/(1 + sqrt(2))^2
arg2 = rec        # 1/(1 + sqrt(2))^2

# Compute dilogarithms
li2_1 = mp.polylog(2, arg1)  # Li_2(1 - rec)
li2_2 = mp.polylog(2, arg2)  # Li_2(rec)

# Compute difference of dilogarithms
diff_li2 = li2_1 - li2_2

# Second term: (1/4) * [Li_2(1 - rec) - Li_2(rec)]
term2 = (1/4) * diff_li2

# Sum both terms
result = term1 + term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))