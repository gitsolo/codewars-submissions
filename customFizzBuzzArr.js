const fizzBuzzCustom = (str1 = 'Fizz', str2 = 'Buzz', num1 = 3, num2 = 5) =>
  Array(100)
    .fill(0)
    .map((i, j) => j + 1)
    .map(i =>
      i % num1 === 0 && i % num2 === 0
        ? str1 + str2
        : i % num1 === 0
        ? str1
        : i % num2 === 0
        ? str2
        : i
    );
