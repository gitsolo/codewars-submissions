const findOdd = f => {
  const obj = {};
  f.forEach(i => {
    obj[i] = [];
  });
  f.forEach((i, j) => {
    obj[i].push(j);
  });
  return Object.keys(obj).filter(i => obj[i].length % 2 !== 0)[0];
};
