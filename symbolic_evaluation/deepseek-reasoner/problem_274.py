import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the coefficient (65*π)/4
coefficient = mp.fmul(65, mp.pi)
coefficient = mp.fdiv(coefficient, 4)

# Compute the modified Bessel function of the first kind I_1(5
bessel_value = mp.besseli(1, 5)

# Multiply coefficient by the Bessel function value
result = mp.fmul(coefficient, bessel_value)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))