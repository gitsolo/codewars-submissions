const obj = {
  0: 0,
  1: 1,
  2: 2,
  3: 3,
  4: 4,
  5: 5,
  6: 6,
  7: 7,
  8: 8,
  9: 9,
  A: 10,
  B: 11,
  C: 12,
  D: 13,
  E: 14,
  F: 15,
};

const convToDeci = num =>
  num
    .split('')
    .reverse()
    .map((i, j) => obj[i] * 16 ** j)
    .reduce((i, j) => i + j);

const hexStringToRGB = color => {
  const col = color.slice(1).toUpperCase();
  return {
    r: convToDeci(col.slice(0, 2)),
    g: convToDeci(col.slice(2, 4)),
    b: convToDeci(col.slice(4, 6)),
  };
};
