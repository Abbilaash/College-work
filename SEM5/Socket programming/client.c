#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_IP "10.1.94.115"
#define SERVER_PORT 8080

int main() {
    int sock = 0;
    struct sockaddr_in server_addr;
    char *message = "Hello from client";
    char buffer[1024] = {0};

    // Step 1: Create socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(SERVER_PORT);

    // Convert IP address from text to binary
    if (inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr) <= 0) {
        perror("Invalid address");
        exit(EXIT_FAILURE);
    }

    // Step 2: Connect to server
    if (connect(sock, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }

    // Step 3: Send data to the server
    send(sock, message, strlen(message), 0);
    printf("Message sent to server: %s\n", message);

    // Step 4: Read the server's response
    read(sock, buffer, sizeof(buffer));
    printf("Server response: %s\n", buffer);

    // Step 5: Close the socket
    close(sock);
    return 0;
}
