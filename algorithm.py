from abc import ABC, abstractmethod
from cache import Cache

class CachingAlgorithm(ABC):

    cache = None

    num_of_hits = 0

    def __init__(self, starting_values, verbose=False):  
        """     
        Args:
            starting_values (list): The starting values of the cache.
            verbose (bool): Whether to print out the steps of the simulation. Defaults to False.
        
        Returns:
            None
        """
        self.cache = Cache(starting_values)
        self.verbose = verbose

    @abstractmethod
    def simulate(self, sequence):
        """
        Simulates the cache with the given sequence.

        Args:
            sequence (list): The sequence of values to run the simulation on.

        Returns:
            None
        """
        pass
    
    def get_hits(self):
        """
        Returns the number of hits in the cache.

        Args:
            None

        Returns:
            int: The number of hits in the cache.
        """
        return self.num_of_hits
