import 'package:trotter/trotter.dart';

void main(List<String> arguments) {
  const length = 14;
  const List<int> numberSet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  Map<int, int> possibleSums = {};
  for (int i = (numberSet.first * length); i <= (numberSet.last * length); i++) {
    possibleSums[i] = 0;
  }

  var comps = Compositions(length, numberSet.toList());
  print('${comps.length} compositions with ${possibleSums.length} possible unique summations.');

  print('Finding summations...');
  for (final composition in comps()) {
    var sum = 0;
    for (final number in composition) {
      sum += number;
    }
    possibleSums[sum] = possibleSums[sum]! + 1;
  }

  for (MapEntry e in possibleSums.entries) {
    print('${e.key}: ${e.value}');
  }

  return;
}
