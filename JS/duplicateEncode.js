const duplicateEncode = str => {
  const arr = str.toLowerCase().split('');
  const obj = {};
  arr.forEach(i => (obj[i] = obj[i] ? obj[i] + 1 : 1));
  return arr.map(i => (obj[i] === 1 ? '(' : ')')).join('');
};
