from Dijkstra import dijkstra, Infinity
import numpy as np
from itertools import combinations
import logging


def get_id_node(node):
    """
        Argument:
            node (array) : sub-list from a combination of [0, 1, 2, ..., n]

        Return:
            get_id_node (int) : describe the unique code integer for this node
    """
    return np.sum(2**node, dtype=int)



def calculate_edge_weigth(node1, node2, time_mages):
    """
        Calculate weight of the edge node1 -> node2.

        Arguments:
            node1 (array) : unique sequence of number that define the node1
            node2 (array) : same for node2
            time_mages (array) : time to travel for each mage

        Return:
            edge_weight (float) : weigth of the edge
    """
    n = len(time_mages)
    all_mages_idxs = np.linspace(0, n-1, n, dtype=int)
    nb_node2 = len(node2)
    nb_node1 = nb_node2 -1

    if nb_node2 == len(all_mages_idxs):
        # last case ENDING - assert(len(idxs_mages_that_come) == 2) is True
        idxs_mages_that_come = [idx for idx in node2 if idx not in node1]
        edge_weight = np.max([time_mages[idxs_mages_that_come[0]], time_mages[idxs_mages_that_come[1]]])
    else:
        if nb_node1 == 0:
            # first case initialization
            node1 = np.array([-1])
        mages_comparison = [idx for idx in node2 if idx in node1]
        mages_difference = [idx for idx in node2 if idx not in node1]
        nb_common = len(mages_comparison)

        if nb_common < nb_node2 - 2:
            edge_weight = Infinity
        elif nb_common == nb_node2 - 2:
            # two mages not present in node2 => two mages pass
            idx_mage_that_go_back = [idx for idx in node1 if idx not in node2][0]
            idxs_mages_that_come = mages_difference
            # we have assert(len(idxs_mages_that_come) == 2) is True
            edge_weight = np.max([time_mages[idxs_mages_that_come[0]], time_mages[idxs_mages_that_come[1]]]) + time_mages[idx_mage_that_go_back]
        elif nb_common == nb_node2 - 1 or nb_node1 == 0:
            # all mages from node1 are in node2 => one mage passes
            idx_mage_to_come = mages_difference[0]
            idxs_mages_escort = [idx for idx in all_mages_idxs if idx not in node2]
            stock = [np.max([time_mages[idx_mage_to_come], time_mages[idx_escort]])+time_mages[idx_escort] for idx_escort in idxs_mages_escort]
            edge_weight = np.min(stock)
    return edge_weight



def construct_graph(n, time_mages, enable_inf=False, disp_info=False):
    """
        Contruct the graph into a good format
        for the input dijkstra function.

        Arguments:
            n (int) : number of mages = len(time_mages)
            time_mages (array) : time to travel for each mage.
            enable_inf (bool) : enable to put infinity in edges, otherwise
                do not consider the edges and make the graph smaller (default)
            disp_info (bool) : display information through logging or not

        Return:
            graph (array) : representation of the graph
                to solve the mages problem.
    """
    if disp_info:
        # activate logging
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    if n <= 0:
        # error
        raise RuntimeError("The number of mages has to be a positive non-zero integer.")
    elif len(time_mages[time_mages <= 0]) != 0 :
        # negative time or equal to zero
        print(time_mages[time_mages <= 0])
        raise RuntimeError("One of the mages travel time is not a positive non-zero integer.")
    elif n <= 2:
        # trivial cases
         return [(1, np.max(time_mages))]
    else:
        # general case
        all_mages_idxs = np.linspace(0, n-1, n, dtype=int)
        nb_nodes_max = 2**n-3 #(2**n -1 -2 -1 + 1) => +1 for the last node
        graph = [[] for _ in range(nb_nodes_max+1)] # +1 for the first node
        for k in range(0, n-1):
            logging.info("Step : " + str(k))
            for i in combinations(all_mages_idxs, k):
                i = np.array(i)
                if k < n-2:
                    for j in combinations(all_mages_idxs, k+1):
                        j = np.array(j)
                        edge_weight = calculate_edge_weigth(i, j, time_mages)
                        if edge_weight != Infinity or enable_inf:
                            logging.info("Edge : " +str(i)+ " -> " + str(j))
                            # do not add the edge in case of infinity useless
                            graph[get_id_node(i)].append((get_id_node(j),edge_weight))
                else:
                    # link all last nodes to the unique last vertice
                    logging.info("Edge : " +str(i)+ " -> END")
                    edge_weight = calculate_edge_weigth(i, all_mages_idxs, time_mages)
                    graph[get_id_node(i)].append((nb_nodes_max,edge_weight))
    logging.info("Graph : " + str(graph)[:int(1e10)] + "...")
    return graph



if __name__ == "__main__":
    # input format as asked
    n = int(input())
    time_mages = np.zeros(n)
    for i in range(n):
        time_mages[i] = float(input())

    # construct graph - n_nodes total = 2**n - n (with enable_inf=True)
    mages_graph = construct_graph(n=n, time_mages=time_mages, disp_info=False, enable_inf=False)

    # calculate the shortest path in graph from node 0 to the the node -1
    shortest_path = dijkstra(nodoI=0, grafo=mages_graph)[-1]

    # display the shortest path
    print(shortest_path)
