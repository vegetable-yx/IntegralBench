import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute arcsinh(7)
a = mp.asinh(7)

# Compute the exponents: (4/3)*a and (2/3)*a
exp1 = (4/3) * a
exp2 = (2/3) * a

# Compute exponential terms: e^{exp1}, e^{-exp1}, e^{exp2}, e^{-exp2}
term1 = mp.exp(exp1)   # e^{(4/3)*asinh(7)}
term2 = mp.exp(-exp1)  # e^{-(4/3)*asinh(7)}
term3 = mp.exp(exp2)   # e^{(2/3)*asinh(7)}
term4 = mp.exp(-exp2)  # e^{-(2/3)*asinh(7)}

# Compute the symmetric sums
sum1 = term1 + term2  # e^{(4/3)a} + e^{-(4/3)a}
sum2 = term3 + term4  # e^{(2/3)a} + e^{-(2/3)a}

# Compute the main expression
# (3/8)*sum1 - (3/4)*sum2 + 3/4
part1 = (3/8) * sum1
part2 = (3/4) * sum2
result = part1 - part2 + 0.75

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))