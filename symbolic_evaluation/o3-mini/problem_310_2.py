import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute term1: (√π / 8) * erfi(1)
sqrt_pi = mp.sqrt(mp.pi)
erfi_1 = mp.erfi(1)
term1 = (sqrt_pi / 8) * erfi_1

# Compute arguments for dilogarithms
sqrt2 = mp.sqrt(2)
arg1 = (sqrt2 - 1) / sqrt2  # (√2 - 1)/√2
arg2 = (sqrt2 + 1) / sqrt2  # (√2 + 1)/√2

# Compute dilogarithms
li2_arg1 = mp.polylog(2, arg1)  # Li₂((√2 - 1)/√2)
li2_arg2 = mp.polylog(2, arg2)  # Li₂((√2 + 1)/√2)

# Compute term2: [Li₂(arg1) - Li₂(arg2)] / 16
diff_li2 = li2_arg1 - li2_arg2
term2 = diff_li2 / 16

# Combine terms for final result
result = term1 + term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))