# https://www.codewars.com/kata/59f897ecc374cb9ed90000c2

def monkey_talk(phrase):
  return(' '.join(['eek' if (i.lower()[0] in ['a', 'e', 'i', 'o', 'u']) else 'ook' for i in phrase.split(' ')]) + '.').capitalize()
