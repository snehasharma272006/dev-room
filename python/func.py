#functions working 
def greet(name):
    print ("Hello", name)
greet("Alice")

def Hello():
    print ("welcome to hospital system ")
Hello()

def check_age(age):
    if (age>=18):
        print ("you are eligible to vote")
    else:
        print ("you are not eligible to vote")

check_age(12)
check_age(20)


#fucntions with return type
def square(num):
    return num*num

print(square(4))


def patient_info(name,age):

    return name,age
name, age = patient_info("sneha", 25)
print(name , "is", age, "years old")



def bmi_calculator(weight, height):
    bmi = weight/(height*height)
    return bmi

bmi = bmi_calculator (65 , 1.55)
print ("your bmi is", bmi)


def check_temp(temp):
    if temp<=99:
        return "normal"
    elif temp>99 and temp<=104:
        return "fever"
    elif temp>105:
        return "high fever"
temp_status = check_temp(101)
print (temp_status)





