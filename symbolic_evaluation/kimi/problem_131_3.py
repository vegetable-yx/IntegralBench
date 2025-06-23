import mpmath as mp
mp.dps = 15

# Calculate square root of 2 for coefficient and Bessel argument
sqrt2 = mp.sqrt(2)

# Compute the argument for the modified Bessel function
bessel_arg = 2 * sqrt2

# Calculate modified Bessel function of the first kind I_1(2√2)
i1_value = mp.besseli(1, bessel_arg)

# Compute the coefficient π/(4√2)
coefficient = mp.pi / (4 * sqrt2)

# Multiply components to get final result
result = coefficient * i1_value

print(mp.nstr(result, n=10))