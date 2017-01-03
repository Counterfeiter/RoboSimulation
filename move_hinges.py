import bpy

#sce = bpy.context.scene
#ob = bpy.context.object

#bpy.ops.ptcache.bake_all(bake=True)

#print(dir(bpy.data.scenes["Scene"].rigidbody_world.constraints.objects["hip_front_r_hinge"].rotation_axis_angle))
print(dir(bpy.context.object.animation_data))
#print(bpy.data.scenes["Scene"].rigidbody_world.constraints.objects["hip_back_r_mot"].rotation_axis_angle[0])

def SetHingeOptions(object):
    object.rigid_body_constraint.breaking_threshold = 0.1
    object.rigid_body_constraint.use_breaking = False
    object.rigid_body_constraint.solver_iterations = 100
    object.rigid_body_constraint.use_override_solver_iterations = True

def SetMotorVelocity(object, velo = 0.0):
    object.rigid_body_constraint.motor_ang_target_velocity = velo
    object.rigid_body_constraint.motor_ang_max_impulse = 5000.0
    if (velo == 0.0):
        object.rigid_body_constraint.use_motor_ang = False
    else:
        object.rigid_body_constraint.use_motor_ang = True
    

def my_handler(scene):
    try:
        my_handler.my_velo += 0.0
        if(bpy.context.scene.frame_current == 1):
            my_handler.my_velo = 0.0
        if(bpy.context.scene.frame_current > 100):
            my_handler.my_velo -= 10.0
    except AttributeError:
        my_handler.my_velo = 0.0  # it doesn't exist yet, so initialize it
        
    SetMotorVelocity(scene.objects["hip_front_l_mot"], my_handler.my_velo)
    print(my_handler.my_velo)
    print(scene.objects["hip_back_r_mot"].matrix_world.translation)
    


def register():
    bpy.app.handlers.frame_change_post.clear()
    bpy.app.handlers.frame_change_post.append(my_handler)

def unregister():
    bpy.app.handlers.frame_change_post.remove(my_handler)
    
SetMotorVelocity(bpy.data.objects["knee_front_l_mot"], 0.0)
SetMotorVelocity(bpy.data.objects["knee_front_r_mot"], 0.0)
SetMotorVelocity(bpy.data.objects["knee_back_l_mot"], 0.0)
SetMotorVelocity(bpy.data.objects["knee_back_r_mot"], 0.0)

SetMotorVelocity(bpy.data.objects["hip_front_l_mot"], 0.0)
SetMotorVelocity(bpy.data.objects["hip_front_r_mot"], 0.0)
SetMotorVelocity(bpy.data.objects["hip_back_l_mot"], 0.0)
SetMotorVelocity(bpy.data.objects["hip_back_r_mot"], 0.0)

SetHingeOptions(bpy.data.objects["knee_front_l_hinge"])
SetHingeOptions(bpy.data.objects["knee_front_r_hinge"])
SetHingeOptions(bpy.data.objects["knee_back_l_hinge"])
SetHingeOptions(bpy.data.objects["knee_back_r_hinge"])

SetHingeOptions(bpy.data.objects["hip_front_l_hinge"])
SetHingeOptions(bpy.data.objects["hip_front_r_hinge"])
SetHingeOptions(bpy.data.objects["hip_back_l_hinge"])
SetHingeOptions(bpy.data.objects["hip_back_r_hinge"])

# get object list
print(bpy.data.objects["hip_back_r_mot"])

register()

