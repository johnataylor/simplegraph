
from .graph import GraphValue

class InferenceRules:

    @staticmethod
    def create_from_schema(schema):
        result = []

        # RDFS refer to https://www.w3.org/TR/rdf-schema/
        result.extend(InferenceRules.range(schema))
        result.extend(InferenceRules.domain(schema))
        result.extend(InferenceRules.subClassOf(schema))
        result.extend(InferenceRules.subPropertyOf(schema))

        # OWL refer to https://www.w3.org/TR/owl-features/
        result.extend(InferenceRules.inverseOf(schema))
        result.extend(InferenceRules.symmetricProperty(schema))
        result.extend(InferenceRules.transitiveProperty(schema))
        result.extend(InferenceRules.sameAs(schema))
        result.extend(InferenceRules.functionalProperty(schema))
        result.extend(InferenceRules.inverseFunctionalProperty(schema))

        return result

    @staticmethod
    def range(schema):
        result = []
        for t in (x for x in schema.get_by_predicate("range") if x.o.is_ref):
            result.append(lambda g: InferenceRules.apply_range(g, t.s, t.o))
        return result
    
    @staticmethod
    def apply_range(g, p, c):
        for t in [x for x in g.get_by_predicate(p) if x.o.is_ref]:
            g.add(t.o.value, "@type", c)

    @staticmethod
    def domain(schema):
        result = []
        for t in (x for x in schema.get_by_predicate("domain") if x.o.is_ref):
            result.append(lambda g: InferenceRules.apply_domain(g, t.s, t.o))
        return result

    @staticmethod
    def apply_domain(g, p, c):
        for t in [x for x in g.get_by_predicate(p) if x.o.is_ref]:
            g.add(t.s, "@type", c)

    @staticmethod
    def subClassOf(schema):
        result = []
        for t in (x for x in schema.get_by_predicate("subClassOf") if x.o.is_ref):
            result.append(lambda g: InferenceRules.apply_subClassOf(g, GraphValue(t.s, True), t.o))
        return result

    @staticmethod
    def apply_subClassOf(g, a, b):
        for t in [x for x in g.get_by_predicate_object("@type", a)]:
            g.add(t.s, "@type", b)

    @staticmethod
    def subPropertyOf(schema):
        return []
        
    @staticmethod
    def inverseOf(schema):
        return []

    @staticmethod
    def symmetricProperty(schema):
        return []

    @staticmethod
    def transitiveProperty(schema):
        return []

    @staticmethod
    def sameAs(schema):
        return []

    @staticmethod
    def functionalProperty(schema):
        return []

    @staticmethod
    def inverseFunctionalProperty(schema):
        return []
