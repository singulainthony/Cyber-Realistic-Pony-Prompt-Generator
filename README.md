# ComfyUI-CyberRealistic-Pony

Custom nodes for generating prompts for Cyber Realistic Pony models in ComfyUI.

## Nodes

- **CyberRealistic Subject** – Build subject prompts (gender, age, ethnicity, body, hair, clothing, pose, etc.).
- **CyberRealistic Master Prompt** – Combine subjects with scene/location/lighting/camera and output positive + negative prompts.

Both appear under the **CyberRealistic Pony** category in the Add Node menu.

## If nodes don’t appear

1. **Restart ComfyUI** so it rescans custom nodes.

2. **Check the ComfyUI terminal** when it starts. Look for:
   - `Import times for custom nodes:`  
     If you see `ComfyUI-CyberRealistic-Pony` with **(IMPORT FAILED)** next to it, there is an import error; the traceback above it will show the cause.
   - If the extension is not listed at all, ComfyUI is not loading from this folder.

3. **Confirm this folder is in ComfyUI’s `custom_nodes` directory**  
   The folder that contains `main.py` and `folder_paths.py` is the ComfyUI root. This repo must be placed as:
   ```
   <ComfyUI root>/custom_nodes/ComfyUI-CyberRealistic-Pony/
   ```
   So that `custom_nodes/ComfyUI-CyberRealistic-Pony/__init__.py` and `nodes.py` exist there.

4. **In the UI**, use **Add Node** and search for **CyberRealistic** or open the **CyberRealistic Pony** category.

5. **Manager / whitelist**  
   If you use ComfyUI Manager and custom nodes are disabled by default, ensure **ComfyUI-CyberRealistic-Pony** is not disabled and is allowed (e.g. whitelisted if you use a whitelist).
