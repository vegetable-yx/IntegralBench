import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical solution is π times the modified Bessel function I_0 evaluated at 1
# Compute I_0(1) - modified Bessel function of the first kind, order 0
bessel_value = mp.besseli(0, 1)

# Multiply by π to get the integral value
result = mp.pi * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))