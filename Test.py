import bpy
from mathutils import Vector

def add_camera(location, rotation):
    # Create a new camera object
    cam_data = bpy.data.cameras.new(name='NewCamera')
    cam_obj = bpy.data.objects.new('NewCamera', cam_data)
    
    # Set camera properties
    cam_obj.location = Vector(location)
    cam_obj.rotation_euler = Vector(rotation)

    # Link camera object to the scene and set it as the active camera
    bpy.context.collection.objects.link(cam_obj)
    bpy.context.scene.camera = cam_obj
    return cam_obj

def render_image(model_path, position, rotation, resolution, output_path):
    # Clear existing objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Import the model
    bpy.ops.import_scene.fbx(filepath=model_path)

    # Set the position and rotation of the object
    obj = bpy.context.selected_objects[0]
    obj.location = position
    obj.rotation_euler = rotation
    obj.scale = (1, 1, 1)

    # Set render resolution
    bpy.context.scene.render.resolution_x = resolution[0]
    bpy.context.scene.render.resolution_y = resolution[1]
    bpy.context.scene.render.resolution_percentage = 100

    # Add a camera if none exists and set its position and rotation
    if 'NewCamera' not in bpy.data.objects:
        cam = add_camera((0, 0, 10), (0, 0, 0))
    else:
        cam = bpy.data.objects['NewCamera']
    

    # Render the image
    bpy.context.scene.render.filepath = output_path
    bpy.ops.render.render(write_still=True)

# Example usage
model_path = 'furry.fbx'
position = (1, 0, 1)  # Change as needed
rotation = (0, 0, 0)  # Euler angles in radians
resolution = (1920, 1080)  # Width x Height
output_path = 'C:/Users/Aunym/Documents/Repositories/runpod-worker-comfyui/ComfyUI_windows_portable/ComfyUI/custom_nodes/image.png'

render_image(model_path, position, rotation, resolution, output_path)
