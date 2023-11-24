import numpy as np

def singleton(class_):
    """
    This decorator turns a class into a singleton. 
    The singleton pattern is a design pattern that restricts the instantiation of a class to one object. 
    This is useful when exactly one object is needed to coordinate actions across the system.
    """
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Zipf():
    """
    This class generates random numbers according to the Zipf distribution.

    The Zipf distribution is a discrete distribution with the following probability mass function:

    .. math::
        P(k) = \\frac{k^{-\\alpha}}{\\sum_{i=1}^{R} i^{-\\alpha}}

    where :math:`R` is the range of values and :math:`\\alpha` is a parameter.

    Attributes:
        computed_values (dict): A dictionary of computed values. The key is a tuple of the parameters :math:`(R, \\alpha)` and the value is the generated sequence.
    """

    computed_values = {}

    def generate(self, R, alpha):
        """
        Generates a sequence of random numbers according to the Zipf distribution.

        Args:
            R (int): The range of values.
            alpha (float): The parameter :math:`\\alpha`.
        
        Returns:
            list: The generated sequence.
        """
        if (R, alpha) in self.computed_values:
            return self.computed_values[(R, alpha)]
        ranked_items = np.arange(1, R + 1)
        probs = ranked_items ** (-alpha)
        probs /= np.sum(probs)
        self.computed_values[(R, alpha)] = np.random.choice(ranked_items, size=R, p=probs, replace=True)
        return self.computed_values[(R, alpha)]
