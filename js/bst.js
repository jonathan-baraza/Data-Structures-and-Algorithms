// Binary Search Tree
class Node {
  constructor(data, left = null, right = null) {
    this.data = data;
    this.left = left;
    this.right = right;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  //fn to add data to the binary search tree
  add(data) {
    const node = this.root;
    if (node === null) {
      this.root = new Node(data);
    } else {
      const searchTree = function (node) {
        if (data < node.data) {
          if (node.left === null) {
            node.left = new Node(data);
            return;
          } else if (node.left !== null) {
            return searchTree(node.left);
          }
        } else if (data > node.data) {
          if (node.right === null) {
            node.right = new Node(data);
            return;
          } else if (node.right !== null) {
            return searchTree(node.right);
          }
        } else {
          return null;
        }
      };
      return searchTree(node);
    }
  }

  //fn to find min
  findMin() {
    let current = this.root;
    while (current.left !== null) {
      current = current.left;
    }
    return current.data;
  }

  //fn to find max
  findMax() {
    let current = this.root;
    while (current.right !== null) {
      current = current.right;
    }
    return current.data;
  }

  //find a node
  find(data) {
    let current = this.root;
    while (current) {
      if (data === current.data) {
        return current;
      }
      if (data < current.data) {
        current = current.left;
      } else {
        current = current.right;
      }
    }
    return null;
  }

  //   check if data is present
  isPresent(data) {
    let current = this.root;
    if (data === current.data) {
      return true;
    }
    if (data < current.data) {
      current = current.left;
    } else {
      current = current.right;
    }

    return false
  }
}
