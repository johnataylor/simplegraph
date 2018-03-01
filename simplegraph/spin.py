
def spin(graph, rules):
    while True:
        before = graph.count
        for rule in rules:
            rule(graph)
        after = graph.count
        if after > before:
            break
