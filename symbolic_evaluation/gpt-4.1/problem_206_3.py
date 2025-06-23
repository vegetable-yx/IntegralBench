import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Compute the integral: ∫₀¹ [exp((-1+i)u²) + exp((1-i)u²)] du
# Step 1: Define the complex parameters
b1 = mp.mpc(-1, 1)   # -1 + i
b2 = mp.mpc(1, -1)    # 1 - i

# Step 2: Compute -b1 and -b2
neg_b1 = -b1
neg_b2 = -b2

# Step 3: Compute square roots of -b1 and -b2
sqrt_neg_b1 = mp.sqrt(neg_b1)
sqrt_neg_b2 = mp.sqrt(neg_b2)

# Step 4: Compute error function terms
erf_term1 = mp.erf(sqrt_neg_b1)
erf_term2 = mp.erf(sqrt_neg_b2)

# Step 5: Compute each integral term using closed-form solution
# term1 = √π / (2 √(-b1)) * erf(√(-b1))
term1 = (mp.sqrt(mp.pi) / (2 * sqrt_neg_b1)) * erf_term1
term2 = (mp.sqrt(mp.pi) / (2 * sqrt_neg_b2)) * erf_term2

# Combine terms for the integral value
integral_value = term1 + term2

# Step 6: Compute the multiplicative factors
# factor1 = π/2 * √π
factor1 = (mp.pi / 2) * mp.sqrt(mp.pi)
# factor2 = e^{iπ/8} / 2^{1/4}
complex_exponential = mp.exp(mp.mpc(0, mp.pi/8))
two_power = mp.power(2, 0.25)  # 2^{1/4}
factor2 = complex_exponential / two_power

# Step 7: Multiply all components
result_complex = factor1 * factor2 * integral_value

# The analytical expression is expected to be real; take the real part
result_real = mp.re(result_complex)

# Print the result to 10 decimal places
print(mp.nstr(result_real, n=10))