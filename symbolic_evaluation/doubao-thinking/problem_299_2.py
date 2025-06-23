import mpmath as mp

mp.dps = 15

a = mp.mpf('0.25')
b = mp.mpf('0.5')

# Compute I1: integral of ln(1-t) term
beta_ab = mp.beta(a, b)
psi_half = mp.psi(b)
psi_3_4 = mp.psi(a + b)
I1 = beta_ab * (psi_half - psi_3_4)

# Compute I3: integral of ln(t) term
psi_1_4 = mp.psi(a)
I3 = beta_ab * (psi_1_4 - psi_3_4)

# Compute I2: integral of ln(1+t) term using series expansion
sum_I2 = mp.mpf(0)
n = 1
eps = mp.mpf('1e-15')
max_terms = 1000

for _ in range(max_terms):
    term = (-1)**(n+1) / n * mp.beta(a + n, b)
    sum_I2 += term
    if mp.fabs(term) < eps:
        break
    n += 1

I2 = sum_I2

# Combine all components and multiply by 2
total_integral = I1 + I2 - I3
result = 2 * total_integral

print(mp.nstr(result, n=10))