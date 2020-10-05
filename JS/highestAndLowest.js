const highAndLow = (str = '9') => {
  const nums = str
    .split(' ')
    .map(Number)
    .sort((a, b) => b - a);

  return `${nums[0]} ${nums[nums.length - 1]}`;
};
