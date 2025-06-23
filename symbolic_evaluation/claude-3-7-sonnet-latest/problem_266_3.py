import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate J_0(1) - Bessel function of the first kind, order 0 at x=1
bessel_value = mp.besselj(0, 1)

# Subtract 1 from the Bessel value
adjusted_value = bessel_value - 1

# Multiply by π/4
result = (mp.pi / 4) * adjusted_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))