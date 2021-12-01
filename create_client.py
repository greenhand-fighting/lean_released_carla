#import carla
import sys
print(sys.path)
sys.path.append(
    "/home/l/carlas/carla/PythonAPI/carla/dist/carla-0.9.11-py3.8-linux-x86_64.egg")
import carla
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
print(client.get_client_version())
print(client.get_server_version())

world=client.get_world()
print(client.get_available_maps())
world = client.load_world('Town01')

weather = carla.WeatherParameters(
    cloudiness=80.0,
    precipitation=30.0,
    sun_altitude_angle=70.0)

world.set_weather(weather)

print(world.get_weather())

# Get the light manager and lights
lmanager = world.get_lightmanager()
mylights = lmanager.get_all_lights()

# Custom a specific light
light01 = mylights[0]
light01.turn_on()
light01.set_intensity(100.0)
state01 = carla.LightState(200.0,carla.Color(255,0,0),carla.LightGroup.Building,True)
light01.set_light_state(state01)




# Turn on position lights
#current_lights = carla.VehicleLightState.NONE
#current_lights |= carla.VehicleLightState.Position
#vehicle.set_light_state(current_lights)


debug = world.debug
#debug.draw_box(carla.BoundingBox(actor_snapshot.get_transform().location,carla.Vector3D(0.5,0.5,2)),actor_snapshot.get_transform().rotation, 0.05, carla.Color(255,0,0,0),0)

# Retrieve a snapshot of the world at current frame.
# 得到当前帧的世界的一个快照
world_snapshot = world.get_snapshot()

timestamp = world_snapshot.timestamp # Get the time reference 

for actor_snapshot in world_snapshot: # Get the actor and the snapshot information
    actual_actor = world.get_actor(actor_snapshot.id)
    actor_snapshot.get_transform()
    actor_snapshot.get_velocity()
    actor_snapshot.get_angular_velocity()
    actor_snapshot.get_acceleration()  
    print(actual_actor)

actor_snapshot = world_snapshot.find(actual_actor.id) # Get an actor's snapshot