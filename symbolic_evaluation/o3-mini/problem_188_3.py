import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant term: π²/16
constant_term = mp.pi**2 / 16

# Compute the denominator D = 13 + √168
D = 13 + mp.sqrt(168)

# Compute the small parameter a = 1/(2*(13+√168))
a = 1 / (2 * D)

# Compute the argument for the gamma functions in numerator: 1+a and 1-a
gamma_num_arg1 = 1 + a
gamma_num_arg2 = 1 - a

# Compute the argument for the gamma functions in denominator: 1/2+a and 1/2-a
gamma_den_arg1 = 0.5 + a
gamma_den_arg2 = 0.5 - a

# Evaluate the gamma functions
gamma_num1 = mp.gamma(gamma_num_arg1)
gamma_num2 = mp.gamma(gamma_num_arg2)
gamma_den1 = mp.gamma(gamma_den_arg1)
gamma_den2 = mp.gamma(gamma_den_arg2)

# Compute the fraction: [Γ(1+a)Γ(1-a)] / [Γ(1/2+a)Γ(1/2-a)]
fraction = (gamma_num1 * gamma_num2) / (gamma_den1 * gamma_den2)

# Take the natural logarithm of the fraction
log_term = mp.log(fraction)

# Compute the coefficient: 1/(8*(13+√168))
coefficient = 1 / (8 * D)

# Multiply the log term by the coefficient
log_part = coefficient * log_term

# Sum the constant term and the logarithmic part
result = constant_term + log_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))