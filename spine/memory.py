# spine/memory.py - Centralized memory management

from memory.vector import VectorMemory
from memory.cache import CacheMemory

class CoreMemory:
    def __init__(self):
        self.vector = VectorMemory()
        self.cache = CacheMemory()
        print("CoreMemory initialized.")

    def store(self, query: str, result):
        # Persist new experience to vector memory and cache.
        self.vector.add(query, result)
        self.cache.set(query, result)

    def recall(self, query: str):
        # Recall experience, checking cache first then vector memory.
        cached = self.cache.get(query)
        if cached:
            return cached

        result = self.vector.get(query) # Changed from search to get
        if result:
            self.cache.set(query, result)
        return result

MEMORY = CoreMemory()
