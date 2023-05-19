const binarySearch = (arr, target) => {
  let newList = [...arr];
  let midpoint;

  while (newList.length > 0) {
    midpoint = newList[Math.floor(newList.length / 2)];
    if (midpoint === target) {
      let result = arr.indexOf(target);
      return result === 0 ? "0" : result;
    } else {
      if (midpoint > target) {
        newList = newList.slice(0, newList.indexOf(midpoint));
      } else {
        newList = newList.slice(newList.indexOf(midpoint + 1));
      }
    }
  }
};

const verifySearch = (result) => {
  result
    ? console.log(`The target was found on index ${result}`)
    : console.log("The target was not found on the provided list.");
};

myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
target = 10;

verifySearch(binarySearch(myArray, target));
