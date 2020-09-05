const splitArr = arr => [
  arr.slice(0, Math.floor(arr.length / 2)),
  arr.slice(Math.floor(arr.length / 2)),
];

const addArr = arr => {
  const arr1 = arr[0];
  const arr2 = arr[1];
  const diff = Math.abs(arr1.length - arr2.length);
  const newArr = [];
  diff !== 0 ? newArr.push(arr2[0]) : null;
  arr1.forEach((i, j) => {
    newArr.push(i + arr2[j + diff]);
  });
  return newArr;
};

const splitAndAdd = (arr, n) => {
  const result = [arr];
  while (n > 0) {
    const newArr = addArr(splitArr(result[0]));
    result[0] = newArr;
    n = n - 1;
  }
  return result[0];
};
