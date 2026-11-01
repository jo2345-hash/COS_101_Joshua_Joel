#Physics Formulas
while True:
    print('PHYSICS FORMULA SELECTOR')
    print('1. Speed')
    print('2. Acceleration')
    print('3. Force')
    print('4. Workdone')
    print('5. Kinetic Energy')
    

    def calculate_speed(distance, time):
        print('Speed = Distance / Time')
        #1. Speed
        speed = distance / time
        print('Speed is:', speed,'m/s')

    def calculate_acceleration(finalvelocity, initialvelocity, time):
        print('Acceleration = (Final Velocity -  Initial velocity) / Time')
        #2. Acceleration
        acc = finalvelocity - initialvelocity / time
        print('Acceleration is:',acc,'m/s^2')

    def calculate_force(mass, acceleration):
        #Force
        print('Force = Mass * Acceleration')
        Force = mass * acceleration
        print('Force is:', Force,'N')

    def calculate_workdone(force, distance):
        print('Workdone = Force * Distance')
        #4. Workdone
        workdone = force * distance
        print('Workdone is:', workdone,'J')

    def calculate_kinetic_energy(mass, velocity):
        print('Kinetic Energy = 1/2* Mass * Velocity**2')
        #5. Kinetic Energy
        print('Kinetic energy is:', ke)

    choice = input('Select a formula(1-5): ')

    if choice == '1':
        distance = float(input('Enter the distance: '))
        time  = int(input('Enter the time: '))
        calculate_speed(distance, time)

    elif choice == '2':
        finalvelocity = float(input('Enter the final velocity: '))
        initialvelocity = float(input('Enter the initial velocity: '))
        time = float(input('Enter the time: '))
        calculate_acceleration(finalvelocity, initialvelocity, time)

    elif choice == '3':
        mass = float(input('Enter the mass: '))
        acceleration = float(input('Enter the acceleration: '))
        calculate_force(mass, acceleration)

    elif choice == '4':
        force = float(input('Enter the force: '))
        distance = float(input('Enter the distance: '))
        calculate_workdone(force, distance)

    elif choice == '5':
        mass = float(input('Enter the mass: '))
        velocity = float(input('Enter the velocity: '))
        ke = 1 / 2 * mass * velocity**2
        calculate_kinetic_energy(mass, velocity)

    else:
            print('Invalid selection') 

    choice2 = input('Do you want to calculate for another variable?(Yes/No)')

    if choice2 == 'no':
        print('Thank You!')
        break

    else:
        print('Enter a valid selection')
        
     



















