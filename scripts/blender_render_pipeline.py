#!/usr/bin/env python3
"""
VibeCode Omni Enterprise - Blender 3D Procedural Generation, Lighting, & Web GLB Export Pipeline.
Can be executed directly inside Blender via `execute_blender_code` (mcp-for-blender)
or via headless CLI: `blender -b -P scripts/blender_render_pipeline.py -- --output scene.glb --render preview.png`
"""

import os
import sys

def build_studio_lighting_and_camera():
    import bpy
    import math

    scene = bpy.context.scene
    scene.render.engine = "CYCLES" if "CYCLES" in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items.keys() else "BLENDER_EEVEE"
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.film_transparent = False

    # Studio 3-Point Lighting Rig
    lights = [
        ("Key_Light", (4.0, -4.0, 5.0), 800.0, (1.0, 0.96, 0.90)),
        ("Fill_Light", (-4.5, -2.5, 3.0), 300.0, (0.85, 0.92, 1.0)),
        ("Rim_Light", (0.0, 5.0, 4.0), 500.0, (1.0, 1.0, 1.0)),
    ]
    for name, loc, energy, color in lights:
        if name not in bpy.data.objects:
            light_data = bpy.data.lights.new(name=name, type="AREA")
            light_data.energy = energy
            light_data.color = color
            light_data.size = 2.5
            light_obj = bpy.data.objects.new(name=name, object_data=light_data)
            bpy.context.collection.objects.link(light_obj)
            light_obj.location = loc

    # Camera Setup with Track-To Constraint
    if "Studio_Camera" not in bpy.data.objects:
        cam_data = bpy.data.cameras.new(name="Studio_Camera")
        cam_data.lens = 50.0
        cam_obj = bpy.data.objects.new("Studio_Camera", cam_data)
        bpy.context.collection.objects.link(cam_obj)
        cam_obj.location = (0.0, -6.5, 3.2)
        cam_obj.rotation_euler = (math.radians(68.0), 0.0, 0.0)
        scene.camera = cam_obj


def export_web_ready_glb(output_path: str):
    import bpy
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        export_format="GLB",
        export_apply=True,
        export_texcoords=True,
        export_normals=True,
        export_materials="EXPORT",
        export_draco_mesh_compression_enable=True,
        export_draco_mesh_compression_level=6,
    )
    print(f"[OK] Exported Draco-compressed web GLB to {output_path}")


def render_preview(render_path: str):
    import bpy
    os.makedirs(os.path.dirname(os.path.abspath(render_path)), exist_ok=True)
    bpy.context.scene.render.filepath = os.path.abspath(render_path)
    bpy.ops.render.render(write_still=True)
    print(f"[OK] Rendered studio preview to {render_path}")


if __name__ == "__main__":
    try:
        import bpy  # type: ignore
        build_studio_lighting_and_camera()
        argv = sys.argv
        if "--" in argv:
            custom_args = argv[argv.index("--") + 1:]
            if "--output" in custom_args:
                idx = custom_args.index("--output") + 1
                if idx < len(custom_args):
                    export_web_ready_glb(custom_args[idx])
            if "--render" in custom_args:
                idx = custom_args.index("--render") + 1
                if idx < len(custom_args):
                    render_preview(custom_args[idx])
    except ImportError:
        print("Run this script inside Blender or via `execute_blender_code` tool in mcp-for-blender.")
