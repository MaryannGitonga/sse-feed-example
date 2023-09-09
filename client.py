from sseclient import SSEClient

# listens for incoming SSE events and prints the event data (simulating the social feed)
def main():
    url = 'http://localhost:5000/feed'

    client = SSEClient(url)
    for event in client:
        print(event.data)

if __name__ == '__main__':
    main() 