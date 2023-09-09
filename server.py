from flask import Flask, Response
import time

server = Flask(__name__)

# Dummy feed data
feed_data = [
    "User 1 posted: Hello, world!",
    "User 2 posted: Enjoying my day!",
    "User 3 posted: #coding",
    "User 1 posted: Enjoying my day too!"
]

# a feed generator function: allows to send the feed data one feed at a time
def event_stream():
    yield "data: New feed updates>>>\n\n"

    for feed in feed_data:
        yield f"data: {feed}\n\n"
        time.sleep(2)  # Simulate new posts every 2 seconds

    yield "data: <<<Your feed is up to date\n\n"

# serves SSE data on the /feed endpoint
# sends each feed as an SSE event to the connected client every 2 seconds
@server.route('/feed')
def sse():
    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    server.run(debug=True)