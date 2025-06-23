import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Bessel function terms
# J_{-1/4}(1/2)
bessel_minus = mp.besselj(-0.25, 0.5)

# J_{1/4}(1/2)
bessel_plus = mp.besselj(0.25, 0.5)

# Compute the difference: J_{-1/4}(1/2) - J_{1/4}(1/2)
diff_bessel = bessel_minus - bessel_plus

# Calculate 2^(7/4)
base = mp.power(2, mp.mpf(7)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply all components: 2^(7/4) * sqrt(pi) * [J_{-1/4}(1/2) - J_{1/4}(1/2)]
result = base * sqrt_pi * diff_bessel

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))