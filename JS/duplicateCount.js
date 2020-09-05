const duplicateCount = str => {
  const obj = {};
  str
    .toLowerCase()
    .split('')
    .forEach(i => (obj[i] = obj[i] + 1 || 1));
  return Object.keys(obj)
    .filter(i => obj[i] > 1)
    .join('');
};
