import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Appell F1 function with the given parameters
# F1(a, b1, b2, c, x, y) = F1(1/2, 1, 1, 2; 1+i, 1-i)
a = mp.mpf('0.5')
b1 = mp.mpf('1')
b2 = mp.mpf('1')
c = mp.mpf('2')
x = mp.mpc(1, 1)  # 1 + i
y = mp.mpc(1, -1) # 1 - i

# Evaluate Appell F1 hypergeometric function
F1_val = mp.appellf1(a, b1, b2, c, x, y)

# Multiply the result by pi
result = mp.pi * F1_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))