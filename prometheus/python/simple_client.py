from prometheus_client import start_http_server, Summary
import random
import time
import argparse

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds',
                       'Time spent processing request')

# Decorate function with metric.


@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p')
    args = parser.parse_args()
    if args.p is None:
        args.p = 8000
    return args


if __name__ == '__main__':
    args = parse()
    # Start up the server to expose the metrics.
    start_http_server(int(args.p))
    # Generate some requests.
    while True:
        process_request(random.random())
