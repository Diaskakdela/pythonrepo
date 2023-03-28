import random
import string


class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


students = {}
# while True:
#     subject = input("Enter subject name (or press Q to quit): ")
#     if subject == "Q":
#         break
#     first_name = input("Enter first name: ")
#     last_name = input("Enter last name: ")
#     grades = list(map(int, input("Enter grades separated by spaces: ").split()))
#     if subject in students:
#         students[subject].append(Student(first_name, last_name, grades))
#     else:
#         students[subject] = [Student(first_name, last_name, grades)]
#
# for subject, student_list in students.items():
#     print(f"Subject: {subject}")
#     student_list.sort(key=lambda x: x.average_grade(), reverse=True)
#     for student in student_list:
#         print(f"{student.first_name} {student.last_name}: {student.average_grade()}")
#     print()

def sortNumsThird():
    nums = list(input("Enter nums separated by space: ").split())
    print(nums.sort())




def sortNumsFourth():
    nums = list(input("Enter nums separated by space: ").split())
    print(sorted(nums, reverse=True))


def secondTask(a, b):
    if (a > b):
        for x in range(a, b - 1, -1):
            print(x)
    else:
        for x in range(a, b + 1):
            print(x)


def lotteryFifthTask(nums):
    flag = True
    for x in nums:
        randInt = random.randint(1, 49)
        print(f"Current num = {x}")
        print(f"Random num = {randInt} \n")
        if (x != random.randint(1, 49)):
            flag = False
    if flag:
        print("Ticket is lucky")
    else:
        print("Ticket is unlucky")


print(lotteryFifthTask([5, 19]))

def sixthTask(lst, reverse=False):
    flag = True
    if reverse:
        return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    else:
        return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

#
# lst = input("Enter nums separated by space: ").split()
# lst = [int(x) for x in lst]
#
# # if sixthTask(lst):
# #     print("List is sorted")
# # else:
# #     print("List is not sorted")
#
# print(sixthTask(lst))