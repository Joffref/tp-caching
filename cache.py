class Cache():
    """
    A cache that stores values and can replace them. It is used as the underlying cache for the algorithms.

    Args:
        values (list): The starting values of the cache.
    
    Returns:
        None
    """
    _values = []

    def __init__(self, values):
        """
        Initializes the cache.

        Args:
            values (list): The starting values of the cache.
        
        Returns:
            None
        """
        self._values = values
    
    def replace(self, old_value, new_value):
        """
        Replaces a value in the cache.

        Args:
            old_value (int): The value to be replaced.
            new_value (int): The value to replace the old value with.
        
        Returns:
            None
        """
        if old_value not in self._values:
            return
        
        if old_value == new_value:
            return
        self._values[self._values.index(old_value)] = new_value
    
    def put_in_front(self, value):
        """
        Puts a value in front of the cache.

        Args:
            value (int): The value to be put in front.
        
        Returns:
            None
        """
        if value == self._values[0]:
            return
        if value in self._values:
            self._values.remove(value)
            self._values = [value] + self._values
            return
        if len(self._values) == 1:
            self._values = [value]
            return
        self._values = [value] + self._values[:-1]

    def is_hit(self, value):
        """
        Checks if a value is in the cache.

        Args:
            value (int): The value to check.
        
        Returns:
            bool: Whether the value is in the cache.
        """
        return value in self._values
    
    def get_cache(self):
        """
        Gets the cache.

        Args:
            None
        
        Returns:
            list: The cache.
        """
        return self._values