# https://www.codewars.com/kata/59d398bb86a6fdf100000031

def string_breakers(n, st):
  return '\n'.join(st.replace(' ', '')[0 + i: i + n] for i in range(0, len(st), n)).strip()
