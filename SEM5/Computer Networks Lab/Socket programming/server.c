#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8080
#define MAX_CLIENTS 5

int main() {
    int server_fd, client_socket, addr_len;
    struct sockaddr_in server_addr, client_addr;
    char buffer[1024] = {0};

    // Step 1: Create socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket failed");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;  // Accept connections from any IP address
    server_addr.sin_port = htons(PORT);

    // Step 2: Bind socket to the IP/PORT
    if (bind(server_fd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // Step 3: Listen for incoming connections
    if (listen(server_fd, MAX_CLIENTS) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }
    printf("Server listening on port %d...\n", PORT);

    // Step 4: Accept a client connection
    addr_len = sizeof(client_addr);
    if ((client_socket = accept(server_fd, (struct sockaddr*)&client_addr, (socklen_t*)&addr_len)) < 0) {
        perror("Client accept failed");
        exit(EXIT_FAILURE);
    }

    printf("Client connected: %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

    // Step 5: Receive and send data
    read(client_socket, buffer, sizeof(buffer));
    printf("Message from client: %s\n", buffer);

    // Respond to client
    send(client_socket, "Hello from server", strlen("Hello from server"), 0);

    // Close connection
    close(client_socket);
    close(server_fd);
    return 0;
}
