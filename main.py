from timeit import default_timer as timer
from dijkstra import dijkstra
from bellmanford import bellmanford
import graph


def main():
    # Initialize input sizes for sparse and dense graphs
    vlist_sparse = [100,
                    200,
                    300,
                    400,
                    500,
                    600,
                    700,
                    800,
                    900,
                    1000
                    ]

    elist_sparse = [200,
                    400,
                    600,
                    800,
                    1000,
                    1200,
                    1400,
                    1600,
                    1800,
                    2000
                    ]

    vlist_dense = [10,
                   20,
                   30,
                   40,
                   50,
                   60,
                   70,
                   80,
                   90,
                   100
                   ]

    elist_dense = [40,
                   160,
                   360,
                   640,
                   1000,
                   1440,
                   1960,
                   2560,
                   3240,
                   4000
                   ]

    print('sparse graphs')
    for v, e in zip(vlist_sparse, elist_sparse):
        print(v, e)
        g = graph.random_connected_graph(v, e)
        s_d_time = 0
        s_b_time = 0
        for i in range(0, 10):
            s_d_start = timer()
            dijkstra(g, 0)
            s_d_end = timer()
            s_d_time += (s_d_end - s_d_start)

            s_b_start = timer()
            bellmanford(g, 0)
            s_b_end = timer()
            s_b_time += (s_b_end - s_b_start)
        print('dtime = ', s_d_time)
        print('avg dtime = ', s_d_time / 10)
        print('btime = ', s_b_time)
        print('avg btime = ', s_b_time / 10)

    print('dense graphs')
    for v, e in zip(vlist_dense, elist_dense):
        print(v, e)
        g = graph.random_connected_graph(v, e)
        d_d_time = 0
        d_b_time = 0
        for i in range(0, 10):
            d_d_start = timer()
            dijkstra(g, 0)
            d_d_end = timer()
            d_d_time += (d_d_end - d_d_start)

            d_b_start = timer()
            bellmanford(g, 0)
            d_b_end = timer()
            d_b_time += (d_b_end - d_b_start)
        print('dtime = ', d_d_time)
        print('avg dtime = ', d_d_time / 10)
        print('btime = ', d_b_time)
        print('avg btime = ', d_b_time / 10)


if __name__ == "__main__":
    main()
