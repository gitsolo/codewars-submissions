// https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/dart

List<String> wave(String x) {
  List<String> arr = x.toLowerCase().split('');

  List<String> result = [];

  for (int i = 0; i < arr.length; i++) {
    if (arr[i] == ' ') {
      continue;
    } else {
      String x = [
        ...arr.sublist(0, i),
        arr[i].toUpperCase(),
        ...arr.sublist(i + 1),
      ].join();
      result.add(x);
    }
  }

  return result;
}
