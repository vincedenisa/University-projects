import random


def gnomeSort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1

    return arr

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):

        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end - 1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1

# generate a list of random natural numbers between 0 and 100
def generateRandomList(n):
    return [random.randint(0,100) for _ in range(n)]

# print the menu
def print_menu():
    print("\nSorting algorithm menu:")
    print("1. Generate a random list of numbers")
    print("2. Sort using Cocktail sort")
    print("3. Sort using Gnome sort")
    print("4. Exit")

# main program
arr=[]
while True:
    print_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        n = int(input("Enter the number of numbers to generate: "))
        arr = generateRandomList(n)
        print("Generated list: ", arr)

    elif choice == "2":
        if not arr:
            print("Please generate a list first!")
        else:
            cocktailSort(arr)
            print("Sorted using Cocktail sort ", arr)

    elif choice == "3":
        if not arr:
            print("Please generate a list first!")
        else:
            gnomeSort(arr, n)
            print("Sorted using Gnome sort: ", arr)

    elif choice == "4":
        print("Exit.")
        break
    else:
        print("Invalid choice!!")


