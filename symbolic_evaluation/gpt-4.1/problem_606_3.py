import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the constant term: pi^2 / 8
pi_sq = mp.pi ** 2
term1 = pi_sq / 8

# Compute the Lerch transcendent value for the series part
# Lerch phi: \Phi(0.5, 2, 0.5) = \sum_{n=0}^{\infty} \frac{(0.5)^n}{(n + 0.5)^2}
z = mp.mpf('0.5')
s_val = mp.lerchphi(z, 2, mp.mpf('0.5'))

# Scale the Lerch transcendent to match the series: S = \sum_{n=0}^{\infty} \frac{1}{(2n+1)^2 2^n} = \Phi(0.5, 2, 0.5)/4
S = s_val / 4

# Compute the entire expression: term1 + sqrt(2) * S
result = term1 + mp.sqrt(2) * S

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))