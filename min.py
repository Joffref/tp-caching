from cache import Cache
from algorithm import CachingAlgorithm

class MinCache(CachingAlgorithm):
    """
    MinCache is a cache that uses the MIN policy to replace values in the cache.

    Args:
        starting_values (list): The starting values of the cache.
        verbose (bool): Whether to print out the steps of the simulation. Defaults to False.
    
    Returns:
        None
    """

    def simulate(self, sequence):
        """
        Simulates the cache with the given sequence.

        Args:
            sequence (list): The sequence of values to run the simulation on.

        Returns:
            None
        """
        step = 1
        for v in sequence:
            if self.verbose:
                print(f" === Step {step} === \nChecking {v}...\nCache: {self.cache.get_cache()}\nSequence: {sequence}")
            step += 1
            if self.cache.is_hit(v):
                self.num_of_hits += 1
                sequence = sequence[1:]
                if self.verbose:
                    print("Hit!\n=====\n\n")
                continue
            self.pop_farthest(sequence)
            sequence = sequence[1:]
            if self.verbose:
                print("Miss!\n=====\n\n")
          
            
    def pop_farthest(self, sequence):
        """
        Pops the farthest value from the cache and replaces it with the first value in the sequence.

        Args:
            sequence (list): The sequence of values to run the simulation on.

        Returns:
            None
        """
        internal_cache = self.cache.get_cache()
        val = -1
        idx = 0
        for c in internal_cache:
            if c not in sequence: # If the value is not in the sequence, it is the farthest
                val = c
                break
            for v in sequence:
                if c == v and idx < sequence.index(v): # If the value is in the sequence, but it is farther than the current farthest, it is the farthest
                    val = c
                    idx = sequence.index(v)
                    break
        if val == -1: # If the value is not in the sequence, and no value in the sequence is farther than the current farthest, replace the farthest with the first value in the sequence
            self.cache.replace(internal_cache[0], sequence[0])
            return    
        self.cache.replace(val, sequence[0])
    
                

