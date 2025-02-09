from dataclasses import dataclass

@dataclass
class NodeNumber:
     value: float

     def __repr__(self):
          return self._repr

     def __post_init__(self):
          self._repr = f"{self.value}"
     
@dataclass
class AddNode:
     node_a: any
     node_b: any

     def __repr__(self):
          return f"({self.node_a}+{self.node_b})"
     
@dataclass
class NodeSubtact:
     node_a: any
     node_b: any

     def __repr__(self):
          return f"({self.node_a}+{self.node_b})"
     
class NodeMultiply:
     node_a: any
     node_b: any

     def __repr__(self):
          return f"({self.node_a}+{self.node_b})"
     
class NodeDivide:
     node_a: any
     node_b: any

     def __repr__(self):
          return f"({self.node_a}+{self.node_b})"