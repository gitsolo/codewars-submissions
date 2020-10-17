const sumOrProduct = (arr = [1], n) => {
  const newArr = arr.sort((a, b) => a - b);

  const sum = newArr.slice(arr.length - n).reduce((i, j) => i + j);

  const product = newArr.slice(0, n).reduce((i, j) => i * j);

  return sum > product ? 'sum' : sum === product ? 'same' : 'product';
};
