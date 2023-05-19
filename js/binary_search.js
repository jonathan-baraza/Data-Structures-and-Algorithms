const binarySearch = (arr, target) => {
  //   My implementation
  //   let newList = [...arr];
  //   let midpoint;
  //   while (newList.length > 0) {
  //     midpoint = newList[Math.floor(newList.length / 2)];
  //     if (midpoint === target) {
  //       let result = arr.indexOf(target);
  //       return result === 0 ? "0" : result;
  //     } else {
  //       if (midpoint > target) {
  //         newList = newList.slice(0, newList.indexOf(midpoint));
  //       } else {
  //         newList = newList.slice(newList.indexOf(midpoint + 1));
  //       }
  //     }
  //   }
  /*
   *
   *
   *
   *
   *
   * */
  //Implementation two

  let myArray = [...arr];
  let highValue = myArray.length - 1;
  let lowValue = 0;
  let midpoint;

  while (lowValue <= highValue) {
    midpoint = Math.floor((lowValue + highValue) / 2);
    // let midpointIndex = Math.floor((low + high) / 2);
    console.log("midpoint");
    console.log(midpoint);
    if (myArray[midpoint] === target) {
      console.log("found hey ", midpoint);
      return midpoint;
    } else {
      if (myArray[midpoint] > target) {
        highValue = midpoint - 1;
      } else {
        lowValue = midpoint + 1;
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
target = 8;

verifySearch(binarySearch(myArray, target));
