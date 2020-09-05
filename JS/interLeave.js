const interleave = (...args) => {
  const lengths = args.map(i => i.length);
  const maxedArr = args.filter(i => i.length === Math.max(...lengths))[0];
  const arr = [];
  maxedArr.forEach((i, j) => {
    args.forEach(k => {
      arr.push(k[j]);
    });
  });
  return arr.map(i => (i === undefined ? null : i));
};
