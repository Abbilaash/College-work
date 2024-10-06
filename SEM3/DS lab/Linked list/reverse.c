#include <stdio.h>

struct Node {
    int data;
    struct Node* next;
};

// Function to reverse the linked list
void reverse(struct Node** head_ref) {
    struct Node* prev = NULL;
    struct Node* current = *head_ref;
    struct Node* next = NULL;
    
    while (current != NULL) {
        next = current->next;   // Store next node
        current->next = prev;   // Reverse the current node's pointer
        prev = current;         // Move pointers one position ahead
        current = next;
    }
    *head_ref = prev;
}

// Function to print linked list
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

// Function to push a node at the beginning
void push(struct Node** head_ref, int new_data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

int main() {
    struct Node* head = NULL;

    push(&head, 20);
    push(&head, 4);
    push(&head, 15);
    push(&head, 85);

    printf("Given Linked List\n");
    printList(head);

    reverse(&head);

    printf("Reversed Linked List\n");
    printList(head);

    return 0;
}
