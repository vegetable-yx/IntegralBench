import mpmath as mp

# Set decimal places for internal calculations to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Compute constant: sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute the argument: 1/(1 + sqrt(2))
x = 1 / (1 + sqrt2)

# Compute the two polylogarithm terms
# term1 = Li_2(1/(1+sqrt(2)))
term1 = mp.polylog(2, x)
# term2 = Li_2(-1/(1+sqrt(2)))
term2 = mp.polylog(2, -x)

# Compute ln(1 + sqrt(2))
ln_val = mp.log(1 + sqrt2)

# Compute the square of ln(1 + sqrt(2))
ln_sq = ln_val ** 2

# Compute pi * ln(1 + sqrt(2))
pi_ln = mp.pi * ln_val

# Combine the terms according to the expression:
# (1/8) * [ -4 * term1 + 4 * term2 + pi_ln + 2 * ln_sq ]
result = (1/8) * (-4 * term1 + 4 * term2 + pi_ln + 2 * ln_sq)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))