def transitive_closure(r):
    def compose_relations(s1, s2):
        return {(a, b) for (a, c1) in s1 for (c2, b) in s2 if c1 == c2}

    def transitive_closure_recursive(current, result):
        next_step = compose_relations(current, r)
        if not next_step.issubset(result):
            result.update(next_step)
            transitive_closure_recursive(next_step, result)

    result = set(r)
    transitive_closure_recursive(r, result)
    return result