function Queue() {
  var collection = [1, 2, 3, 4];
  var collection2 = [
    ["cat", 1],
    ["dog", 3],
  ];
  this.print = () => {
    console.log(collection);
  };

  this.enqueue = (element) => {
    collection.push(element);
  };

  this.enqueuePriority = (element) => {
    var added = false;
    for (var i = 0; i < collection2.length; i++) {
      if (element[1] < collection2[i][1]) {
        //checking priorities
        collection2.splice(i, 0, element);
        added = true;
        break;
      }
    }
    if (!added) {
      collection.push(element);
    }
  };

  this.dequeue = () => {
    return collection.shift();
  };
  this.front = () => {
    return collection[0];
  };

  this.size = () => {
    return collection.length;
  };

  this.isEmpty = () => {
    return collection.length === 0;
  };
}

const myQueue = new Queue();
myQueue.enqueue(5);
myQueue.dequeue();
myQueue.print();
myQueue.size();
console.log(myQueue.isEmpty());
