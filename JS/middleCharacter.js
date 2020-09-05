const getMiddle = str => {
  const arr = str.split('');
  const middle = arr.length / 2;
  return arr.length % 2 === 0
    ? arr.slice(middle - 1, middle + 1).join('')
    : arr.slice(middle, middle + 1).join('');
};

console.log(getMiddle('testin'));
