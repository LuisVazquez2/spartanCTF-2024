import socket

payloadExample = """Launching computational intelligence benchmarks.

Please respond to each question with an immediate response. If a reply takes too long, the test will be terminated.

469781228248661089 + 956089083196549134 = 2342342352"""

def solve_challenge():
    # Connect to the server
    server_address = ('0.cloud.chals.io', 24386)
    with socket.create_connection(server_address) as sock:
        while True:
            # Receive the challenge
            challenge = sock.recv(1024).decode()
            print(challenge)
            s = "NO COMPUTATIONAL ERRORS DETECTED. TEST SUCCESS."
            if s in challenge:
                sock.sendall(b"2\n")
                print(sock.recv(1024).decode())
                break
            #wait for the challenge
            while " = " not in challenge:
                challenge = sock.recv(1024).decode()
                print(challenge)
            print(challenge)
            # Extract onyl the numbers from the challenge
            numbers = [int(n) for n in challenge.split() if n.isnumeric()]
            # print(numbers)
            # Calculate the sum of the numbers
            result = sum(numbers)
            print(result)
            # Send the result back to the server
            sock.sendall(f"{result}\n".encode())

if __name__ == "__main__":
    solve_challenge()
