import ast
tree = ast.parse("vals[10]")
for node in ast.walk(tree):
    if isinstance(node, ast.Subscript):
        print("Found Subscript")
        print("node.value:", type(node.value))
        if isinstance(node.value, ast.Name):
            print("list_name:", node.value.id)
        print("node.slice:", type(node.slice))
        if hasattr(node, "slice") and isinstance(node.slice, ast.Constant):
            print("idx_val:", node.slice.value)
