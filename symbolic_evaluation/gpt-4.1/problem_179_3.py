import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the integrand function: f(x) = 1/(x*(2-x)**2) * J1(x) * J2(2-x)
def integrand(x):
    denom = x * (2 - x)**2
    j1 = mp.besselj(1, x)
    j2 = mp.besselj(2, 2 - x)
    return 1 / denom * j1 * j2

# Compute the integral numerically from 0 to 2
# Note: The integrand has singularities at x=0 and x=2, so we use adaptive quadrature
result, _ = mp.quad(integrand, [0, 2], error=True, maxdegree=20)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))