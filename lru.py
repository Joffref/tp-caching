from algorithm import CachingAlgorithm

class LRU(CachingAlgorithm):
    """
    LRU is a cache that uses the LRU policy to replace values in the cache.

    Args:
        starting_values (list): The starting values of the cache.
        verbose (bool): Whether to print out the steps of the simulation. Defaults to False.

    Returns:
        None
    """
    
    def simulate(self, sequence):
        step = 1
        for v in sequence:
            step += 1
            if self.verbose:
                print(f" === Step {step} === \nChecking {v}...\nCache: {self.cache.get_cache()}\nSequence: {sequence}")
            if self.cache.is_hit(v): # If the value is in the cache, put it in front
                self.cache.put_in_front(v)
                sequence = sequence[1:]
                self.num_of_hits += 1
                if self.verbose:
                    print("Hit!\n=====\n\n")
                continue
            self.cache.put_in_front(v) # If the value is not in the cache, put it in front
            if self.verbose:
                print("Miss!\n=====\n\n")