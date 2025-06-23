import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (user must set these values)
a = mp.mpf('1.0')   # Example value, replace as needed
b = mp.mpf('1.0')   # Example value, replace as needed

# Compute a^{3/2}
a_power = a ** mp.mpf('3/2')

# Compute the argument for the hypergeometric function: (a^2 * b^2)/4
arg = (a**2 * b**2) / 4

# Compute the confluent hypergeometric limit function {}_0F_1(5/2; arg)
hyp_val = mp.hyp0f1(mp.mpf('5/2'), arg)

# Multiply components: (2/3) * a^{3/2} * {}_0F_1 result
result = (mp.mpf('2') / mp.mpf('3')) * a_power * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))