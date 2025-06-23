import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute I2: \int_0^{\pi/6} \frac{\sin\theta\,\cos^2\theta}{\sqrt{1-0.0625 \sin^2\theta}} d\theta
# Using the closed-form expression derived via substitution
I2 = 16 * (1 - mp.sqrt(mp.mpf(63)/64)

# Compute the part: \frac{\sqrt{3}}{4} \arcsin(0.125)
part1 = (mp.sqrt(3) / 4) * mp.asin(mp.mpf(1)/8)

# Compute I1: \int_0^{\pi/6} \arcsin(0.25\sin\theta) d\theta using series expansion
I1 = mp.mpf(0)
n = 0
a = mp.mpf(1)/4  # 0.25
tol = mp.mpf(1e-25)  # Tolerance for series convergence

while n < 100:  # Set a maximum of 100 terms to prevent infinite loops
    # Binomial coefficient C(2n, n)
    binom_coeff = mp.binomial(2*n, n)
    # Denominator: 4^n * (2n+1)
    denominator = (4**n) * (2*n + 1)
    # Factor: binom_coeff / denominator
    factor1 = binom_coeff / denominator
    # Factor: a^(2n+1) = (1/4)^(2n+1)
    factor2 = a**(2*n + 1)
    # Incomplete beta function: \int_0^{1/4} t^n (1-t)^{-1/2} dt
    beta_val = mp.betainc(n+1, 0.5, 0, mp.mpf(1)/4)
    # Term: factor1 * factor2 * (1/2) * beta_val
    term = factor1 * factor2 * mp.mpf(0.5) * beta_val
    I1 += term
    # Break if term is below tolerance
    if mp.fabs(term) < tol:
        break
    n += 1

# Combine the parts: I1 + part1 - (1/4)*I2
total = I1 + part1 - (mp.mpf(1)/4) * I2

# Final result: (1/8) * total
result = total / 8

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))