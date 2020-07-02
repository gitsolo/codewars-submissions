const solution = str =>
  str
    .split(/([A-Z])/g)
    .map(i => (i.match(/[A-Z]/g) ? ' ' + i : i))
    .join('');
