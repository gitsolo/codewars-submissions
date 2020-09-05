// https://www.codewars.com/kata/5ce6728c939bf80029988b57/train/dart

bool solve(String name) {
  final List<String> arr = name.split('');
  arr.sort();

  int req = 1;

  if (arr.length != arr.toSet().length) {
    return false;
  }

  for (var i = 0; i < arr.length; i++) {
    var first = arr[i];
    var second = i + 1 >= arr.length
        ? String.fromCharCode(arr.last.codeUnitAt(0) + 1)
        : arr[i + 1];

    if (second.codeUnitAt(0) - first.codeUnitAt(0) != 1) {
      req = 0;
      break;
    }
  }

  return (req == 1);
}
