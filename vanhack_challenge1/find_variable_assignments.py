import ast


def find_variable_assignments(source, target_var_names):
    tree = ast.parse(source)

    violations = set()
    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            if node.name in target_var_names:
                violations.add(node.name)

            for arg in node.args.args:
                if arg.arg in target_var_names:
                    violations.add(arg.arg)

            for n in node.body:
                if isinstance(n, ast.Assign):
                    for e in (a for a in n.targets if isinstance(a, (ast.Tuple, ast.Tuple))):
                        for name in (b for b in e.elts if isinstance(b, ast.Name)):
                            if name.id in target_var_names:
                                violations.add(name.id)

        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and (target.id in target_var_names):
                    violations.add(target.id)

        if isinstance(node, ast.ClassDef):
            if node.name in target_var_names:
                violations.add(node.name)


    return violations
