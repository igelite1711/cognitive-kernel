
"""
Phase 4 — Memory Interface
Provides persistent and cached memory access for the spine.
"""

from memory.vector import VectorMemory
from memory.cache import CacheMemory


class MemoryManager:
    def __init__(self):
        self.vector = VectorMemory()
        self.cache = CacheMemory()

    def recall(self, query: str):
        """Retrieve relevant past knowledge."""
        cached = self.cache.get(query)
        if cached is not None:
            return cached

        result = self.vector.search(query)
        if result:
            self.cache.set(query, result)
        return result

    def store(self, query: str, result):
        """Persist new experience."""
        self.vector.add(query, result)
        self.cache.set(query, result)


# Global memory instance (identity continuity)
MEMORY = MemoryManager()
