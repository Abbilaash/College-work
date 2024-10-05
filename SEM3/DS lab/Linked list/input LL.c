#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int main() {
    int n, value;
    struct Node *head = NULL, *temp = NULL, *newNode = NULL;

    // Ask for the number of nodes
    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    // For loop to create and input nodes
    for (int i = 0; i < n; i++) {
        printf("Enter data for node %d: ", i + 1);
        scanf("%d", &value);

        // Create a new node
        newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = value;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;  // First node becomes the head
        } else {
            temp->next = newNode;  // Link the new node to the previous one
        }
        temp = newNode;  // Move temp to the new node
    }

    // Print the linked list
    printf("The linked list is: ");
    temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");

    return 0;
}
