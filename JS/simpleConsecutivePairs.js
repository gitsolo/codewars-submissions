const isPair = ([x, y]) => Math.abs(x - y) === 1;

const pairs = arr => {
  const newArr = [];

  arr.forEach((_, j) =>
    j % 2 === 0 ? newArr.push(arr.slice(j, j + 2)) : null
  );

  return newArr.map(isPair).filter(i => i).length;
};
