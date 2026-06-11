import traceback
import ast

def get_list_and_idx(exc, source_line):
    list_obj = None
    idx_val = None
    list_name = None
    idx_name = None
    
    try:
        # strip to avoid IndentationError
        tree = ast.parse(source_line.strip())
        for node in ast.walk(tree):
            if isinstance(node, ast.Subscript):
                if isinstance(node.value, ast.Name):
                    list_name = node.value.id
                elif isinstance(node.value, ast.List):
                    list_name = "<list literal>"
                    
                if hasattr(node, "slice") and isinstance(node.slice, ast.Constant):
                    idx_val = node.slice.value
                elif hasattr(node, "slice") and isinstance(node.slice, ast.Name):
                    idx_name = node.slice.id
                break
    except Exception as e:
        print(e)
        pass
        
    tb = exc.__traceback__
    frame = None
    while tb:
        frame = tb.tb_frame
        tb = tb.tb_next
        
    if frame:
        l_dict = frame.f_locals
        g_dict = frame.f_globals
        
        if list_name and list_name in l_dict:
            list_obj = l_dict[list_name]
        elif list_name and list_name in g_dict:
            list_obj = g_dict[list_name]
            
        if idx_name and idx_name in l_dict:
            idx_val = l_dict[idx_name]
        elif idx_name and idx_name in g_dict:
            idx_val = g_dict[idx_name]
            
    return list_obj, idx_val

def test_func():
    fruits = ["🍎", "🍌", "🍇"]
    idx = 10
    return fruits[idx]

try:
    test_func()
except IndexError as e:
    l_obj, i_val = get_list_and_idx(e, "    return fruits[idx]")
    print(f"List: {l_obj}, index: {i_val}")
