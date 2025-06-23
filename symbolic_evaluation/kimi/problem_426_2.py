import mpmath as mp
mp.dps = 15

# Calculate the first term: \frac{1}{2}
term1 = mp.mpf(1)/2

# Calculate the second term: \frac{1}{\pi}
term2 = mp.mpf(1)/mp.pi

# Compute the exponential part: e^{-4\pi}
exp_part = mp.exp(-4 * mp.pi)

# Compute the sine part: \sin(2\pi)
sin_part = mp.sin(2 * mp.pi)

# Compute the final expression: \frac{1}{2} + \frac{1}{\pi} e^{-4\pi} \sin(2\pi)
result = term1 + term2 * exp_part * sin_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))