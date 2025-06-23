import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the two polylog terms
# term1 = Li_2(e^{-2i})
term1 = mp.polylog(2, mp.exp(-2 * mp.j))
# term2 = Li_2(e^{2i})
term2 = mp.polylog(2, mp.exp(2 * mp.j))

# Compute the difference: term1 - term2
diff = term1 - term2

# Multiply by i/4
complex_result = (mp.j / 4) * diff

# The expression is real; extract the real part
result = complex_result.real

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))