# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

def is_pangram(s):
  alphabets = ''.join([chr(i) for i in range(97, 122 + 1)])
  phrase = ''.join(
      sorted(set([i for i in s.lower() if ord(i) >= 97 and ord(i) <= 122])))

  return phrase == alphabets
