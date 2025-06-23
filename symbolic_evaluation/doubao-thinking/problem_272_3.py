import mpmath as mp
mp.dps = 15

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute ln(1 + sqrt(2))
ln_term = mp.log(1 + sqrt2)

# Combine terms inside the parentheses
inner_expr = sqrt2 - 1 + ln2 - ln_term

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * inner_expr

print(mp.nstr(result, n=10))