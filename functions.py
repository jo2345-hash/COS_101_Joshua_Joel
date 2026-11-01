def calculate_velocity(distance, time):
    #Velocity
 
    velocity = distance / time
    print('Velocity is: ', velocity)
# calculate_velocity()


#Functions: A reusabe block of code that executes when called
def calculate_area(radius):
    #Area of a circle
    area = 3.14 * radius * radius
    print('Area is: ', area)
# calculate_area()

choice = input('Enter v to calculate velocity or a to calculate area of a circle: ')

if choice == 'v':
    distance = float(input('Enter the distance: '))
    time = int(input('Enter the time: '))
    calculate_velocity(distance, time)

elif choice == 'a':
     radius = float(input('Enter the radius: '))
     calculate_area(radius)
     


