import bpy

# Set up your animation logic here
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 1))
cube = bpy.context.object
cube.scale = (1, 1, 2)

# Add animation
cube.location = (0, 0, 1)
cube.keyframe_insert(data_path="location", frame=1)

cube.location = (5, 0, 1)
cube.keyframe_insert(data_path="location", frame=50)

# Render settings
bpy.context.scene.render.filepath = './output/animation.mp4'
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'

# Render animation
bpy.ops.render.render(animation=True)
