def calculate_velocity():
    #Velocity
    distance = float(input('Enter the distance: '))
    time = float(input('Enter the time: '))
    velocity = distance / time
    print('Velocity is: ', velocity)



#Functions: A reusabe block of code that executes when called
def calculate_area():
    #Area of a circle
    radius = float(input('Enter the radius: '))
    area = 3.14 * radius * radius
    print('Area is: ', area)


choice = input('Enter v to calculate velocity or a to calculate area of a circle: ')

if choice == 'v':
    print(calculate_velocity())

elif choice == 'a':
    print(calculate_area())

else:
    print('Select the correct variable')