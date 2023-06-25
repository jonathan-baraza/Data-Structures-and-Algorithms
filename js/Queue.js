function Queue() {
  var collection = [];
  const print = () => {
    console.log(collection);
  };

  const enqueue = (element) => {
    collection.push(element);
  };

  const dequeue = () => {
    return collection.shift();
  };
  const front = () => {
    return collection[0];
  };

  const size = () => {
    return collection.length;
  };

  //   const isEmpty = () => {
  //     return collection.length === 0;
  //   };
}
