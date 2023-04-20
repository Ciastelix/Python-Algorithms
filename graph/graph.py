from typing import Dict, List, Any, Optional, Callable, Set
from vertex import Vertex
from edge import Edge
from edgetype import EdgeType
from queue import Queue
import graphviz


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = {}

    def create_vertex(self, data: Any) -> Vertex:
        vertex = Vertex(data, len(self.adjacencies))
        self.adjacencies[vertex] = []
        return vertex

    def add_directed_edge(
        self, source: Vertex, destination: Vertex, weight: Optional[float] = None
    ) -> None:
        edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(
        self, source: Vertex, destination: Vertex, weight: Optional[float] = None
    ) -> None:
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(
        self,
        edge: EdgeType,
        source: Vertex,
        destination: Vertex,
        weight: Optional[float] = None,
    ) -> None:
        if edge == EdgeType.directed:
            self.add_directed_edge(source, destination, weight)
        elif edge == EdgeType.undirected:
            self.add_undirected_edge(source, destination, weight)
        else:
            raise ValueError("Invalid edge type.")

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        queue: Queue[Vertex] = Queue()
        visited: Set[Vertex] = set()
        queue.append(self.adjacencies.keys()[0])
        while len(queue) > 0:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                visit(vertex)
                for edge in self.adjacencies[vertex]:
                    queue.append(edge.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        visited: Set[Vertex] = set()
        for vertex in self.adjacencies.keys():
            self._traverse_depth_first(vertex, visited, visit)

    def _traverse_depth_first(
        self,
        vertex: Vertex,
        visited: Set[Vertex],
        visit: Callable[[Any], None],
    ) -> None:
        if vertex not in visited:
            visited.add(vertex)
            visit(vertex)
            for edge in self.adjacencies[vertex]:
                self._traverse_depth_first(edge.destination, visited, visit)

    def show(self) -> None:
        graph = graphviz.Digraph()
        for vertex in self.adjacencies.keys():
            graph.node(str(vertex.data))
            for edge in self.adjacencies[vertex]:
                graph.edge(
                    str(edge.source.data), str(edge.destination.data), str(edge.weight)
                )
        graph.render("graph.gv", view=True)

    def __str__(self) -> str:
        result = ""
        for vertex in self.adjacencies.keys():
            result += f"{vertex} -> {self.adjacencies[vertex]}"
        return result
