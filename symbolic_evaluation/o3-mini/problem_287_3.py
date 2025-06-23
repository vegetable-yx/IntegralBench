import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute the base expression: 1 + sqrt(2)
base = 1 + sqrt2

# Calculate the two arguments for polylogarithms
arg1 = 1 / base          # 1/(1+sqrt(2))
arg2 = sqrt2 / base      # sqrt(2)/(1+sqrt(2))

# Compute the natural logarithm: ln(1+sqrt(2))
ln_val = mp.log(base)

# Compute dilogarithms (Li_2) for both arguments
li2_arg1 = mp.polylog(2, arg1)
li2_arg2 = mp.polylog(2, arg2)

# Compute trilogarithms (Li_3) for both arguments
li3_arg1 = mp.polylog(3, arg1)
li3_arg2 = mp.polylog(3, arg2)

# Calculate the expression inside the brackets:
# term1 = Li_3(arg1) - Li_3(arg2)
term1 = li3_arg1 - li3_arg2

# term2 = ln_val * [Li_2(arg2) - Li_2(arg1)]
term2 = ln_val * (li2_arg2 - li2_arg1)

# Combine terms for the bracket
bracket = term1 + term2

# Multiply by 1/8
result = bracket / 8

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))