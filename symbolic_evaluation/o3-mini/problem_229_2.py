import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the arguments for the polylogarithms
arg1 = 1 - sqrt2  # 1 - √2
arg2 = 1 + sqrt2  # 1 + √2

# Calculate the trilogarithms (Li3)
Li3_arg1 = mp.polylog(3, arg1)
Li3_arg2 = mp.polylog(3, arg2)

# Compute part1: [Li3(1-√2) - Li3(1+√2)] / 16
part1 = (Li3_arg1 - Li3_arg2) / 16

# Calculate ln(1+√2)
ln_term = mp.log(arg2)

# Compute part2: (π² / 16) * ln(1+√2)
pi_sq = mp.pi**2
part2 = (pi_sq / 16) * ln_term

# Compute part3: [ln(1+√2)]^3 / 12
ln_cubed = ln_term**3
part3 = ln_cubed / 12

# Combine the parts: part1 - part2 + part3
result = part1 - part2 + part3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))