#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>  // for inet_pton

#define PORT 8080
#define MAX_BUFFER_SIZE 1024

void error(const char *msg) {
    perror(msg);
    exit(1);
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr;
    char buffer[MAX_BUFFER_SIZE];

    // Create socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        error("Error opening socket");
    }

    // Set up the server address structure
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    if (inet_pton(AF_INET, "10.1.94.176", &server_addr.sin_addr) <= 0) {  // Use inet_pton instead of inet_addr
        error("Error in inet_pton");
    }
    server_addr.sin_port = htons(PORT);

    // Connect to the server
    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        error("Error connecting to server");
    }

    // Print connection message
    printf("[EchoClient] Connected to server.\n");

    // Main communication loop
    while (1) {
        // Get message from user input
        printf("Enter message: ");
        fgets(buffer, MAX_BUFFER_SIZE, stdin);
        buffer[strcspn(buffer, "\n")] = 0;  // Remove newline character
        
        // Send message to server
        int n = write(sockfd, buffer, strlen(buffer));
        if (n < 0) {
            error("Error writing to socket");
        }

        // If the message is "bye", terminate the chat
        if (strncmp(buffer, "bye", 3) == 0) {
            printf("[EchoClient] Echoed by server: bye\n");
            printf("[EchoClient] Chat ended.\n");
            break;
        }

        // Receive the echoed message from the server
        memset(buffer, 0, MAX_BUFFER_SIZE);
        n = read(sockfd, buffer, MAX_BUFFER_SIZE - 1);
        if (n < 0) {
            error("Error reading from socket");
        }

        // Print the echoed message
        printf("[EchoClient] Echoed by server: %s\n", buffer);
    }

    // Close the socket
    close(sockfd);
    return 0;
}
