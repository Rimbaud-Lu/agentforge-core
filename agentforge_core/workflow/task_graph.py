from __future__ import annotations


class TaskGraph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node_id: str, payload: dict) -> None:
        self.nodes.append({"id": node_id, "payload": payload})

    def add_edge(self, from_node: str, to_node: str) -> None:
        self.edges.append({"from": from_node, "to": to_node})

    def to_dict(self) -> dict:
        return {"nodes": self.nodes, "edges": self.edges}
