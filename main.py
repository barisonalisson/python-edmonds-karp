from edmonds_karp import EdmondsKarp

def main():
    # Define a capacity matrix representing the graph
    capacity = [
        [0, 10, 5, 0, 0, 0],
        [0, 0, 15, 10, 0, 0],
        [0, 0, 0, 5, 10, 0],
        [0, 0, 0, 0, 10, 10],
        [0, 0, 0, 0, 0, 15],
        [0, 0, 0, 0, 0, 0]
    ]

    source = 0  # Starting node
    sink = 5    # Target node

    # Create an EdmondsKarp instance and compute the max flow
    ek = EdmondsKarp(capacity)
    max_flow = ek.find_max_flow(source, sink)

    # Display the result
    print(f"Maximum flow from node {source} to node {sink}: {max_flow}")

if __name__ == "__main__":
    main()
