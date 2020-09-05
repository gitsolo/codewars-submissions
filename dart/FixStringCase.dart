// https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/dart

String solve(String name) {
  final List<String> arr = name.split('');
  final List<int> unicodes = arr.map((e) => e.codeUnitAt(0)).toList();

  final int upper =
      unicodes.where((element) => element >= 65 && element <= 90).length;
  final int lower = unicodes.where((element) => element >= 97).length;

  if (upper > lower) {
    return name.toUpperCase();
  }

  return name.toLowerCase();
}
