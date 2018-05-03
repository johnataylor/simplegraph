
# encoding: utf-8

"""A type to represent, query, and manipulate a Uniform Resource Identifier."""

from .graph import Graph, GraphValue, Triple, print_graph
from .rules import domain, range, inverseOf
from .inference_rules import InferenceRules
from .spin import spin

__all__ = [
            'Graph',
            'GraphValue',
            'Triple',
            'print_graph',
            'InferenceRules',
            'spin',
]