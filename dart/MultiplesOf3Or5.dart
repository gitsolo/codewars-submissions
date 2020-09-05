// https://www.codewars.com/kata/514b92a657cdc65150000006/train/dart

int solution(int n) {
  List<int> arr = [];

  if (n > 0) {
    for (int i = 0; i < n; i++) {
      if (i % 3 == 0 && i % 5 == 0) {
        arr.add(i);
      } else if (i % 3 == 0) {
        arr.add(i);
      } else if (i % 5 == 0) {
        arr.add(i);
      }
    }
    return arr.reduce((value, element) => value + element);
  }

  return 0;
}
