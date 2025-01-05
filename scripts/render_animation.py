import bpy

# Load the script and set the voiceover as a placeholder
script_file = "output/script.txt"
with open(script_file, "r", encoding="utf-8") as f:
    script_text = f.read()

# Customize the animation
bpy.data.texts["AnimationText"].from_string(script_text)
bpy.context.scene.render.filepath = "output/animation.mp4"

# Render the animation
bpy.ops.render.render(animation=True)
