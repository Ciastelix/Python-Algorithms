from typing import Optional
from vertex import Vertex


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]
