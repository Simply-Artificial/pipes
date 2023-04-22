from .exceptions import InvalidNodeType

from pathlib import Path

__all__ = ["SADispatchPathway", "SADispatchPathingCollection"]


class SADispatchPathway:
    def __init__(
            self,
            name: str,
            sa_node_type: str,
            location: Path,
    ) -> None:
        self.name: str = name
        self.location: Path = location
        self.sa_node_type: str = sa_node_type

        if not self.location.exists():
            self.location.open("w").close()

    def __repr__(self) -> str:
        return str({
            "name": self.name,
            "sa_node_type": self.sa_node_type,
            "location": self.location,
        })


class SADispatchPathingCollection:
    def __init__(self, nodes: list[SADispatchPathway]) -> None:
        self._nodes: dict[str, SADispatchPathway] = {} if nodes is None else {node.name: node for node in nodes}

    def __repr__(self) -> str:
        return str(self._nodes)

    def get(self, name: str) -> SADispatchPathway:
        return self._nodes[name]

    def add(self, node: SADispatchPathway) -> None:
        self._nodes[node.name] = node

    def remove(self, name: str) -> None:
        del self._nodes[name]
