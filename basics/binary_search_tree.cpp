#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int inf = 0x3f3f3f3f;


struct node {
  int data;
  struct node *left;
  struct node *right;
};


struct node * newnode(int x){
  struct node * temp = (node*)malloc(sizeof(node));
  temp->data = x;
  temp->left = temp->right = NULL;
  return temp;
}


struct node * insert(struct node* root, int x){
  if (root == NULL) { return newnode(x); }
  else {
    if (x <= root->data){
      root->left = insert(root->left, x);
    } else {
      root->right = insert(root->right, x);
    }
    return root;
  }
}


int tree_height(struct node * node){
  if (node == NULL){ return 0; }
  else{
    int ld = tree_height(node->left);
    int rd = tree_height(node->right);
    return (ld > rd ? ld+1:rd+1);
  }
}


// pre/post/in order traversals

void preorder(struct node *root){
  if (root){
    cout << root->data << "\n";
    preorder(root->left);
    preorder(root->right);
  }
}

void postorder(struct node *root){
  if (root){
    postorder(root->left);
    postorder(root->right);
    cout << root->data << "\n";
  }
}

void inorder(struct node *root){
  if (root){
    inorder(root->left);
    cout << root->data << "\n";
    inorder(root->right);
  }
}


int main(){
  struct node *tree = newnode(5);
  insert(tree, 4);
  insert(tree, 3);
  insert(tree, 2);
  insert(tree, 6);
  insert(tree, 8);
  insert(tree, 7);
  insert(tree, 9);
  inorder(tree);

  cout << "tree height: " << tree_height(tree) << "\n";

  return 0;
}