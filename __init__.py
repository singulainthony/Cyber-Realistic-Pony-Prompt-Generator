"""
ComfyUI-CyberRealistic-Pony: Prompt generator nodes for Cyber Realistic Pony models.
"""
import os
import importlib.util

# Load nodes.py from this package directory (works regardless of package context)
_this_dir = os.path.dirname(os.path.abspath(__file__))
_nodes_path = os.path.join(_this_dir, "nodes.py")
_spec = importlib.util.spec_from_file_location("ComfyUI_CyberRealistic_Pony_nodes", _nodes_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

NODE_CLASS_MAPPINGS = _mod.NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = getattr(_mod, "NODE_DISPLAY_NAME_MAPPINGS", {})

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
