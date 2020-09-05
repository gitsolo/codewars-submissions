const obj = {
  0: '0',
  1: '1',
  2: '2',
  3: '3',
  4: '4',
  5: '5',
  6: '6',
  7: '7',
  8: '8',
  9: '9',
  10: 'A',
  11: 'B',
  12: 'C',
  13: 'D',
  14: 'E',
  15: 'F',
};

const convToHex = num => {
  const arr = [];
  let x = num;
  if (num === 0) {
    return '00';
  }
  while (Math.floor(x / 16 > 0)) {
    arr.push(x % 16);
    x = Math.floor(x / 16);
  }
  const f = arr
    .map(i => obj[i])
    .reverse()
    .join('');
  return f.length === 1 ? 0 + f : f;
};

const rgb = (r, g, b) => {
  const arr = [r, g, b];
  return arr
    .map(i => (i > 255 ? convToHex(255) : i < 0 ? convToHex(0) : convToHex(i)))
    .join('');
};
