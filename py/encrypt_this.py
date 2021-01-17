# https://www.codewars.com/kata/5848565e273af816fb000449/train/python

def encrypt_this(text):
  if (text == ''):
    return ''

  arr = text.split(' ')
  newArr = []

  for i in arr:
    s = f"{ord(i[0])}"
    if(len(i) > 1):
      if (len(i) == 2):
        s = s + i[1]
      elif (len(i) == 3):
        s = s + i[-1] + i[1]
      else:
        s = s + i[-1] + i[2:-1] + i[1]

    newArr.append(s)

  return ' '.join(newArr)
