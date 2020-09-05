// https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/dart

int find(List<int> arr) {
  bool set1 = arr[0] % 2 == 0 && arr[1] % 2 == 0;
  bool set2 = arr[1] % 2 == 0 && arr[2] % 2 == 0;
  bool set3 = arr[2] % 2 == 0 && arr[0] % 2 == 0;

  if (set1 || set2 || set3) {
    List<int> x = arr.where((element) => element % 2 != 0).toList();
    return x[0];
  }

  List<int> x = arr.where((element) => element % 2 == 0).toList();
  return x[0];
}
