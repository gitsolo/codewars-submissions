const reverseLetter = str =>
  str
    .split('')
    .map(i => (i.match(/[A-Za-z]/gi) ? i : null))
    .filter(i => i !== null)
    .reverse()
    .join('');
