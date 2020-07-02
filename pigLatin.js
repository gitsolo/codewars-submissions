const pigIt = str =>
  str
    .split(' ')
    .map(i => (i.match(/[A-Za-z]/g) ? i.slice(1) + i[0] + 'ay' : i))
    .join(' ');
