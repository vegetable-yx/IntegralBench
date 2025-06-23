import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate constants
sqrt_pi = mp.sqrt(mp.pi)
sqrt2 = mp.sqrt(2)

# Compute the logarithm term: ln((sqrt2 + 1)/2)
log_term = mp.log((sqrt2 + 1) / 2)

# Compute the imaginary error function at 1
erfi1 = mp.erfi(1)

# Compute term1: sqrt(pi) * erfi(1) * log_term
term1 = sqrt_pi * erfi1 * log_term

# Compute arguments for polylogarithms
arg1 = 1 - sqrt2
arg2 = 1 - 1/sqrt2

# Compute polylog(2) for the arguments
li1 = mp.polylog(2, arg1)
li2 = mp.polylog(2, arg2)

# Compute the difference between polylog terms
dilog_diff = li1 - li2

# Compute term2: (sqrt2 / 4) * (li1 - li2)
term2 = (sqrt2 / 4) * dilog_diff

# Sum both terms
result = term1 + term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))