// https://www.codewars.com/kata/563e320cee5dddcf77000158/train/dart

int getAverage(List<int> nums) =>
    (nums.reduce((value, element) => value + element)) ~/ nums.length;
