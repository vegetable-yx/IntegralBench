import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the exponential factor: e^{-1/2}
exp_factor = mp.exp(-0.5)

# Calculate the modified Bessel functions at 1/2
bessel_neg = mp.besseli(-0.25, 0.5)  # I_{-1/4}(1/2)
bessel_pos = mp.besseli(0.25, 0.5)   # I_{1/4}(1/2)

# Compute the difference: I_{-1/4}(1/2) - I_{1/4}(1/2)
bessel_diff = bessel_neg - bessel_pos

# Multiply by π and the exponential factor
result = mp.pi * exp_factor * bessel_diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))