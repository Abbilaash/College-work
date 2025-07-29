#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>  // for inet_pton
#include <sys/wait.h>  // for wait

#define PORT 8080
#define MAX_BUFFER_SIZE 1024

void error(const char *msg) {
    perror(msg);
    exit(1);
}

int main() {
    int server_sock, client_sock;
    socklen_t client_len;
    struct sockaddr_in server_addr, client_addr;
    char buffer[MAX_BUFFER_SIZE];
    pid_t pid;

    // Create socket
    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock < 0) {
        error("Error opening socket");
    }

    // Set up the server address structure
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    if (inet_pton(AF_INET, "10.1.94.176", &server_addr.sin_addr) <= 0) {  // Use inet_pton instead of inet_addr
        error("Error in inet_pton");
    }
    server_addr.sin_port = htons(PORT);

    // Bind the socket
    if (bind(server_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        error("Error on binding");
    }

    // Listen for incoming connections
    listen(server_sock, 5);
    client_len = sizeof(client_addr);

    // Print waiting message
    printf("[EchoServer] Waiting for client...\n");

    // Accept the incoming connection
    client_sock = accept(server_sock, (struct sockaddr *)&client_addr, &client_len);
    if (client_sock < 0) {
        error("Error on accept");
    }

    // Print client connected message
    printf("[EchoServer] Client connected.\n");

    // Fork a child process to handle client communication
    pid = fork();
    if (pid == 0) {  // Child process
        while (1) {
            // Clear buffer and receive message from client
            memset(buffer, 0, MAX_BUFFER_SIZE);
            int n = read(client_sock, buffer, MAX_BUFFER_SIZE - 1);
            if (n < 0) {
                error("Error reading from socket");
            }

            // Print received message on server side
            printf("[EchoServer] Message received: %s\n", buffer);

            // Echo the message back to client
            n = write(client_sock, buffer, strlen(buffer));
            if (n < 0) {
                error("Error writing to socket");
            }

            // Check if the message is "bye", then terminate the communication
            if (strncmp(buffer, "bye", 3) == 0) {
                break;
            }
        }
        close(client_sock);
        exit(0);
    } else {  // Parent process
        close(client_sock);
        wait(NULL);  // Wait for child process to finish
    }

    // Close the server socket
    close(server_sock);
    return 0;
}
