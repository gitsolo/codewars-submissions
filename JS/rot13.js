const range = arr =>
  Array(Math.abs(arr[1] - arr[0]) + 1)
    .fill(Math.min(...arr))
    .map((i, j) => j + i);

const encodings = arg => {
  const obj = {};
  const arr =
    arg === 'upper'
      ? range(['A'.charCodeAt(), 'Z'.charCodeAt()])
      : range(['a'.charCodeAt(), 'z'.charCodeAt()]);
  arr.forEach(i => {
    const g = i + 13 > arr[arr.length - 1] ? i - 13 : i + 13;
    obj[String.fromCharCode(i)] = g;
  });
  return obj;
};

const rot13 = str => {
  const encodingUpper = encodings('upper');
  const encodingLower = encodings('');

  return str
    .split('')
    .map(i =>
      i.match(/[a-z]/g)
        ? String.fromCharCode(encodingLower[i])
        : i.match(/[A-Z]/g)
        ? String.fromCharCode(encodingUpper[i])
        : i
    )
    .join('');
};
