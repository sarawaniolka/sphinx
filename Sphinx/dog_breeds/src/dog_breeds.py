class Breed():
    """
    This class defines a dog breed
    """

    def __init__(self):
        self.name = None
        self.origin = None
        self.height = None
        self.group = dict()
        
    def describe_breed(self):
        """
        Shows the breed name and group
        
         Usage:
         
        .. doctest::
        
           >>> import dog_breeds
           >>> dog = dog_breeds.Labrador() 
           >>> dog.describe_breed()  
           This dog is a Labrador Retriever.
           It is from Newfoundland.
           >>>
        """
        print(f"This dog is a {self.name}.")
        print(f"It is from {self.origin}.")
        
        
class Labrador(Breed):
    """
    The Labrador Retriever or simply Labrador is a British breed of retriever gun dog.
    Along with :class:`Golden`, :class:`Toller` and :class:`WSS` is one of the 
    VIII group: Retrievers - Flushing Dogs - Water Dogs
    """
    def __init__(self):
        self.name = "Labrador Retriever"
        self.origin = "Newfoundland"
        self.height = 62
        self.group = {"VIII": "Retrievers - Flushing Dogs - Water Dogs"}
        
class Golden(Breed):
    """
    The Golden Retriever is a Scottish breed of retriever dog of medium size.
    Along with :class:`Labrador`, :class:`Toller` and :class:`WSS` is one of the 
    VIII group: Retrievers - Flushing Dogs - Water Dogs.
      
    """
    def __init__(self):
        self.name = "Golden Retriever"
        self.origin = "Great Britain"
        self.height = 61
        self.group = {"VIII": "Retrievers - Flushing Dogs - Water Dogs"}
        
class Toller(Breed):
    """
    The Nova Scotia Duck Tolling Retriever is a medium-sized gundog bred primarily for hunting.
    Along with :class:`Golden`, :class:`Labrador` and :class:`WSS` is one of the 
    VIII group: Retrievers - Flushing Dogs - Water Dogs.
      
    """
    def __init__(self):
        self.name = "Nova Scotia Duck Tolling Retriever"
        self.origin = "Yarmouth County"
        self.height = 54
        self.group = {"VIII": "Retrievers - Flushing Dogs - Water Dogs"}
        
class WSS(Breed):
    """
    The Welsh Springer Spaniel is a breed of dog and a member of the spaniel family. 
    Along with :class:`Golden`, :class:`Toller` and :class:`Labrador` is one of the 
    VIII group: Retrievers - Flushing Dogs - Water Dogs.
      
    """
    def __init__(self):
        self.name = "Welsh Springer Spaniel"
        self.origin = "Wales"
        self.height = 48
        self.group = {"VIII": "Retrievers - Flushing Dogs - Water Dogs"}