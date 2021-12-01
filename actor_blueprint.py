#import carla
import sys
print(sys.path)
sys.path.append(
    "/home/l/carlas/carla/PythonAPI/carla/dist/carla-0.9.11-py3.8-linux-x86_64.egg")
import carla
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)
# 得到蓝图库
blueprint_library = world.get_blueprint_library()

# Find a specific blueprint.
collision_sensor_bp = blueprint_library.find('sensor.other.collision')
# Choose a vehicle blueprint at random.
vehicle_bp = random.choice(blueprint_library.filter('vehicle.*.*'))

# 每一个蓝图有一系列的属性，通过get和set对属性进行设置
is_bike = [vehicle.get_attribute('number_of_wheels') == 2]
if(is_bike)
    vehicle.set_attribute('color', '255,0,0')

for attr in blueprint:  # 遍历蓝图
    if attr.is_modifiable:  # 看这个属性是不是可更改的
        blueprint.set_attribute(attr.id, random.choice(attr.recommended_values))  # 如果可以更改，那么从推荐的值中选择一个

transform = Transform(Location(x=230, y=195, z=40), Rotation(yaw=180))  # 这里给出spawn的地址和朝向
actor = world.spawn_actor(blueprint, transform)  # 开始spawn一个actor

spawn_points = world.get_map().get_spawn_points()  # 给出一些推荐的，可以放置车辆的地点
spawn_point = carla.Transform()
spawn_point.location = world.get_random_location_from_navigation()  # 对于行人，给出一个人行道上的可以放置人的地点，和一个终点

camera = world.spawn_actor(camera_bp, relative_transform, attach_to=my_vehicle, carla.AttachmentType.Rigid)  # 把camera放置在vehicle上

actor_list = world.get_actors()  # 一旦放置在世界中，就可以通过这个函数找到actor！
# Find an actor by id.
actor = actor_list.find(id)
# Print the location of all the speed limit signs in the world.
for speed_sign in actor_list.filter('traffic.speed_limit.*'):
    print(speed_sign.get_location())



print(actor.get_acceleration())
print(actor.get_velocity())

location = actor.get_location()
location.z += 10.0
actor.set_location(location)   # 也是通过get和set来管理世界中的actor的

destroyed_sucessfully = actor.destroy() # Returns True if successful  # python文件结束，actor并不会自动销毁，需要我们手动进行销毁


camera_bp = blueprint_library.find('sensor.camera.rgb')
camera = world.spawn_actor(camera_bp, relative_transform, attach_to=my_vehicle)  # 产生一个相机
camera.listen(lambda image: image.save_to_disk('output/%06d.png' % image.frame))  # 相机存储数据到disk上


settings = world.get_settings()
settings.fixed_delta_seconds = None # Set a variable time-step
world.apply_settings(settings)  # 设置时间步长

settings = world.get_settings()
settings.fixed_delta_seconds = 0.05
world.apply_settings(settings) # 设置固定的时间步长