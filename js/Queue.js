function Queue() {
  var collection = [1, 2, 3, 4];
  this.print = () => {
    console.log(collection);
  };

  this.enqueue = (element) => {
    collection.push(element);
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
