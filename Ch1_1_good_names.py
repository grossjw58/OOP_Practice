
'''
One of the greatest sins when trying to write "clean code" is using misleading names for your variables and functions. 
Take a look at the destroy_wall function. Based on its name, you might assume that it destroys a single wall, 
but if you look closely, you'll see that it handles multiple walls.

The test suite expects a different function name. 
Take a look at the main_test.py file to see what it's looking for, and rename the function accordingly
Additionally, try to rename the variables inside the function to be more descriptive. After passing the tests, 
take a look at the solution to see how we named everything.
'''
##their original function
def destroy_wall(wall_health):
    for w in wall_health:
        if w <= 0:
            wall_health.remove(w)
    return wall_health

##my remade function 
def update_walls_list(wall_health_list: list[int]) -> list[int]:
    for wall_health in wall_health_list:
        if wall_health <= 0:
            wall_health_list.remove(wall_health)
    return wall_health_list

##their recommended function
def destroy_walls(wall_health):
    for w in wall_health:
        if w <= 0:
            wall_health.remove(w)
    return wall_health