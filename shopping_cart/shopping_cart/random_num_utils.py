import random
import string

class RandomUtils:
    """
    Class for generation of random numbers
    """

    @staticmethod
    def generate_random_id() -> str:
        """
        Generate a random ID number of length 6 as a string
        """
        
        return ''.join(random.choices(string.ascii_uppercase, k=6))
    


rnd = RandomUtils()

print(rnd.generate_random_id())  # Example usage
