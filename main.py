from min import MinCache
from lru import LRU
from zipf import Zipf

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def simulate_min():
    alphas = [0.8, 1.0, 1.2]
    sizes = [100, 500, 1000]
    cache_sizes_percent = [1, 10, 20]

    results = [[], [], [], []]

    zipf = Zipf()
    for i in range(0, 5):
        print(f"Trial: {i}\n")
        for alpha in alphas:
            for size in sizes:
                for cache_size in cache_sizes_percent:

                    print(f"Testing with alpha: {alpha}, size: {size}, cache_size: {cache_size}\n")

                    generated_sequence = zipf.generate(size, alpha)
                    num_of_values = int(len(generated_sequence) * (cache_size/100))
                    starting_cache = list(generated_sequence[:num_of_values])
                    sequence = list(generated_sequence[num_of_values:])

                    c = MinCache(starting_cache)
                    c.simulate(sequence)

                    hit_rate = c.get_hits()/len(sequence)

                    results[0].append(alpha)
                    results[1].append(size)
                    results[2].append(cache_size)
                    results[3].append(hit_rate)
                
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = ax.scatter( 
        results[0],
        results[1],
        results[2],
        c=results[3], 
        cmap=plt.viridis()
    )
    fig.colorbar(img)
    plt.show()

def simulate_lru():
    alphas = [0.8, 1.0, 1.2]
    sizes = [100, 500, 1000]
    cache_sizes_percent = [1, 10, 20]

    results = [[], [], [], []]

    zipf = Zipf()
    for i in range(0, 5):
        print(f"Trial: {i}\n")
        for alpha in alphas:
            for size in sizes:
                for cache_size in cache_sizes_percent:

                    print(f"Testing with alpha: {alpha}, size: {size}, cache_size: {cache_size}\n")

                    generated_sequence = zipf.generate(size, alpha)
                    num_of_values = int(len(generated_sequence) * (cache_size/100))
                    starting_cache = list(generated_sequence[:num_of_values])
                    sequence = list(generated_sequence[num_of_values:])

                    l = LRU(starting_cache)
                    l.simulate(sequence)

                    hit_rate = l.get_hits()/len(sequence)
                    
                    results[0].append(alpha)
                    results[1].append(size)
                    results[2].append(cache_size)
                    results[3].append(hit_rate)
                
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = ax.scatter( 
        results[0],
        results[1],
        results[2],
        c=results[3], 
        cmap=plt.viridis()
    )
    fig.colorbar(img)
    plt.show()


if __name__ == "__main__":
    usage = """
    Usage: python main.py [options]

    Options:
        -h, --help      Show this screen.
        -m, --min       Run the example simulation for the Min algorithm.
        -l, --lru       Run the example simulation for the LRU algorithm.
        -s, --simulate  Run the example simulation for both algorithms.
        -z, --zipf      Run the simulation for both algorithms with Zipf distribution. It will take a while.
        -zM, --zipf-min Run the simulation for the Min algorithm with Zipf distribution. It will take a while.
        -zL, --zipf-lru Run the simulation for the LRU algorithm with Zipf distribution. It will take a while.
    """
    import sys
    if len(sys.argv) == 1:
        print(usage)
        sys.exit(0)
    if "-h" in sys.argv or "--help" in sys.argv:
        print(usage)
        sys.exit(0)
    if "-m" in sys.argv or "--min" in sys.argv:
        c = MinCache([1,2,3], True)
        c.simulate([4, 1, 2, 1, 5, 3, 4, 4, 1, 2, 3])

        print(f"Number of hits: {c.get_hits()}")
        sys.exit(0)
    
    if "-l" in sys.argv or "--lru" in sys.argv:
        l = LRU([1,2,3], True)
        l.simulate([4, 1, 2, 1, 5, 3, 4, 4, 1, 2, 3])

        print(f"Number of hits: {l.get_hits()}")
        sys.exit(0)
    
    if "-s" in sys.argv or "--simulate" in sys.argv:
        print("Min algorithm:")
        c = MinCache([1,2,3], True)
        c.simulate([4, 1, 2, 1, 5, 3, 4, 4, 1, 2, 3])

        print(f"Number of hits: {c.get_hits()}\n\n")
        print("LRU algorithm:")

        l = LRU([1,2,3], True)
        l.simulate([4, 1, 2, 1, 5, 3, 4, 4, 1, 2, 3])

        print(f"Number of hits: {l.get_hits()}\n\n")
        sys.exit(0)
    
    if "-z" in sys.argv or "--zipf" in sys.argv:
        simulate_min()
        simulate_lru()
        sys.exit(0)
    
    if "-zM" in sys.argv or "--zipf-min" in sys.argv:
        simulate_min()
        sys.exit(0)
    
    if "-zL" in sys.argv or "--zipf-lru" in sys.argv:
        simulate_lru()
        sys.exit(0)
    
    
