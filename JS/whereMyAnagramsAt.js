const anagrams = (word, words) =>
  words.filter(
    i => i.split('').sort().join('') === word.split('').sort().join('')
  );
