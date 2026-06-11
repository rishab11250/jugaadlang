import ast

def get_list_and_index(source_line):
    try:
        tree = ast.parse(source_line)
        for node in ast.walk(tree):
            if isinstance(node, ast.Subscript):
                list_name = None
                if isinstance(node.value, ast.Name):
                    list_name = node.value.id
                
                idx_name_or_val = None
                if isinstance(node.slice, ast.Constant):
                    idx_name_or_val = node.slice.value
                elif isinstance(node.slice, ast.Name):
                    idx_name_or_val = node.slice.id
                
                return list_name, idx_name_or_val
    except Exception:
        pass
    return None, None

print(get_list_and_index("print(fruits[idx])"))
print(get_list_and_index("vals[10]"))
