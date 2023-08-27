
def create(path):
    path = "Sem8\\phone_book.txt"

    try:
        file = open(path, "r")
    except IOError:
        print("Создан новый справочник -> phone_book.txt ")
        file = open(path, "w")
    finally:
        file.close()




def add_contact(file_name, stroka):
    data = open(file_name, "a")
    data.write(stroka + "\n")
    data.close


def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close

def search(file_name, stroka):
    a = 0
    data = open(file_name, "r")
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print("Нет такого")
    data.close()

def deletecontact(file_name, stroka):

    # data = open(file_name, "r")
    # with open("file_name", "r") as f:

    # # code to delete a particular
    # # data from a file

    # # open file in read mode
    # # with open("sample.txt", "r") as f:
	
	# # read data line by line
	#     data = f.readlines()
        
    # # open file in write mode
    # # input(str("Введите фамилию человека которого хотите удалить"))
    # with open("file_name", "r") as f:
        
    #     for line in data :
            
    #         # condition for data to be deleted
    #         if line.strip("\n") != "Age : 20" :#input(str("Введите фамилию человека которого хотите удалить")): #"Age : 20" :
    #              f.write(line)
    with open(file_name, "r") as data:
        lines = data.readlines()
    with open(file_name, "w") as data:
        for line in lines:
            if stroka not in line:
                data.write(line)
        print("С успехом удалили")  

def change_name(file_name, old_name, new_name):
    with open(file_name, "r+") as data:
        lines = data.readlines()
        for line in lines:
            if old_name in line:
                line = line.replace(old_name, new_name)
                data.write(line)
        print("Данные успешно изменены")

