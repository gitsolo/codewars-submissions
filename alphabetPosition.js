const alphabetPosition = text =>
  text
    .toLowerCase()
    .split('')
    .filter(i => i.match(/[a-z]/g))
    .map(i => i.charCodeAt() - 96)
    .join(' ');
