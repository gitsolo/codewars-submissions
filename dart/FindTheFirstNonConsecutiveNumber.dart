// https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/dart

int firstNonConsecutive(List<int> arr) {
  if (arr.length == 0 || arr.length == 1) {
    return null;
  }

  int req;

  for (var i = 0; i < arr.length; i++) {
    var first = arr[i];
    var second = i + 1 >= arr.length ? arr.last : arr[i + 1];

    if (second - first != 1) {
      req = second;
      break;
    }
  }

  if ((req == arr.last) && ((arr.last - arr[arr.length - 2]) == 1)) {
    return null;
  }

  return req;
}
