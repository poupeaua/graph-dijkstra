from hogwarts import *


# global variable defining time mages to test
TIME_MAGES_TO_TEST = [[np.array([40, 30, 40, 50, 50, 75, 120, 40]), 560],
                     [np.array([1, 2, 5, 8]), 15],
                     [np.array([1, 3, 4, 5]), 14],
                     [np.array([3, 1, 6, 8, 12]), 29],
                     [np.array([1, 2, 5, 10, 12]), 25],
                     [np.array([5, 10, 20, 25]), 60],
                     [np.array([2, 5, 3, 7, 9, 4, 6]), 40],
                     [np.array([1, 2, 5, 10]), 17]]


if __name__ == "__main__":
    print("Running tests...")
    for current_test in TIME_MAGES_TO_TEST:
        time_mages, expected_output = current_test[0], current_test[1]

        n=len(time_mages)

        # construct graph - n_nodes total = 2**n - n (with enable_inf=True)
        mages_graph = construct_graph(n=n, time_mages=time_mages)

        # calculate the shortest path in graph from node 0 to the the node -1
        shortest_path = dijkstra(nodoI=0, grafo=mages_graph)[-1]

        # make the test
        print("Time found =", shortest_path, "| Expected =", expected_output)
        assert(shortest_path == expected_output)
    print("Done")
