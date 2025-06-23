import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument: 1/sqrt(2)
arg = 1 / mp.sqrt(2)

# Compute Bessel functions of the first kind
# J_{-1/4}(arg)
bessel_minus = mp.besselj(-0.25, arg)
# J_{1/4}(arg)
bessel_plus = mp.besselj(0.25, arg)

# Calculate the difference between the two Bessel functions
diff_bessel = bessel_minus - bessel_plus

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * diff_bessel

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))