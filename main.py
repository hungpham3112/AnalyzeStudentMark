from lib import *

if __name__ == "__main__":
    flag = True
    while flag:
        file_name = input("Enter a class to grade (i.e. class1 for class1.txt): ")
        file = f"{file_name}.txt"
        answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
        mark_array = np.array([])
        try:
            with open(file, "r"):
                print(f"\nSuccessfully opened {file}\n")
        except FileNotFoundError:
            print("\nFile not found. Try again!!!\n")
            continue
        mark_array = analyzize(file, answer_key, mark_array)
        report(file, mark_array)
        class_result(file, file_name, answer_key)
