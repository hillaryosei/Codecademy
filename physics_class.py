train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

#write function that converts fahrenheit to celsius
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#test function w/ 100 degrees F
f100_in_celsius=f_to_c(100)
#print(f100_in_celsius)

#write function that converts celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#test function w/ 0 degreese C
c0_in_fahrenheit=c_to_f(0)
#print(c0_in_fahrenheit)

#define function that takes mass and acceleration
def get_force(mass, acceleration):
  return mass * acceleration

#test function
train_force=get_force(train_mass,train_acceleration)
print(train_force)

#print following string:
print(f"The GE train supplies {train_force} Newtons of force.")

#define function that takes in mass and c (constant set to speed of light)
def get_energy(mass,c=3*10**8):
  return mass*c**2

#test function
bomb_energy=get_energy(bomb_mass)
#print(bomb_energy)

#print following string:
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

#define function that takes mass, acceleratin, and distance
def get_work(mass,acceleration,distance):
  force=get_force(mass,acceleration)
  return force * distance

#test function
train_work=get_work(train_mass,train_acceleration,train_distance)
#print(train_work)

#print following sting:
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
