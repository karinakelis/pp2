def main():
    #name,house  = get_student()
    student = get_student()
    print(f"{student[0]} from {student[1]}")
    
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name,house) 
    

#when using a tuple you can not change the values 


'''def get_name():
    return input ("Name: ")

def get_house():
    return input("House: ")'''

if __name__ == "__main__":
    main()