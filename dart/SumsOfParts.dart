// https://www.codewars.com/kata/5ce399e0047a45001c853c2b/train/dart

List<int> partsSums(List<int> arr) {
  if (arr.length == 0) {
    return [0];
  }

  int sum = arr.reduce((value, element) => value + element);
  List<int> sums = [sum];

  arr.forEach((element) {
    sum = sum - element;
    sums.add(sum);
  });

  return sums;
}
