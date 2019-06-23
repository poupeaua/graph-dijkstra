from hogwarts import *


# global variable defining time mages to test
TIME_MAGES_TO_TEST = [np.array([40, 30, 40, 50, 50, 75, 120, 40]),
                     np.array([4059, 5600, 8900, 5100, 10210, 5522, 45820]),
                     np.array([59, 50, 80, 5, 10, 55, 450]),
                     np.array([1, 2, 5, 8]),
                     np.array([1, 3, 4, 5]),
                     np.array([3, 1, 6, 8, 12]),
                     np.array([1, 2, 5, 10, 12]),
                     np.array([5, 10, 20, 25]),
                     np.array([2, 5, 3, 7, 9, 4, 6]),
                     np.array([1, 2, 5, 10])]


def solve(t):
    """
        Solution of the problem found on the internet.
    """
    n = len(t)
    t.sort()                       # increasing order
    if n == 0:                     # special cases
        return 0, []
    elif n == 1:
        return t[0], [t[0]]
    elif n == 2:
        return t[1], [(t[0], t[1])]
    total = (n - 2) * t[0] + sum(t[1:])
    x = n
    threshold = 2 * t[1] - t[0]    # consider edge exchanges
    while t[x - 2] > threshold:
        total -= t[x - 2] - threshold
        x -= 2
    seq = []                       # will be actual crossing sequence
    i = n - 1                      # start from end
    while i > 1:
        if i >= x:
            seq += [(t[0], t[1]), t[1], (t[i - 1], t[i]), t[0]]
            i -= 2
        else:
            seq += [(t[0], t[i]), t[0]]
            i -= 1
    seq.append((t[0], t[1]))       # final crossing
    return total, seq



if __name__ == "__main__":
    print("Running tests...")
    for time_mages in TIME_MAGES_TO_TEST:

        n=len(time_mages)

        # construct graph - n_nodes total = 2**n - n (with enable_inf=True)
        mages_graph = construct_graph(n=n, time_mages=time_mages)

        # calculate the shortest path in graph from node 0 to the the node -1
        shortest_path = dijkstra(nodoI=0, grafo=mages_graph)[-1]
        expected_output, _ = solve(t=time_mages)

        # make the test
        print("Time found =", shortest_path, "| Expected =", expected_output)
        assert(shortest_path == expected_output)
    print("Done")
