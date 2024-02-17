import time
import sys

filepath='product.txt'
with open(filepath, 'r') as file:
    data = file.readlines()

class Products:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

Items = []
ItemsOriginalData = []
info = [line.strip().split(', ') for line in data]

for words in info:
    tempItem = Products(int(words[0]), words[1], float(words[2]), words[3])
    Items.append(tempItem)
    ItemsOriginalData.append(tempItem)
    #print(tempItem)
     
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j].price > arr[j+1].price:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            #print(f"Step {i*n+j+1}: {Items}")
        if not swapped:
            break

def analyzeSortPerformance(data, description, time_complexity):
    #print(f"\n{description} - Starting array: {data}")
    start = time.time()
    #Items.sort(key=lambda x: x.price, reverse=True)
    bubbleSort(data)
    end = time.time()
    space_complexity = sys.getsizeof(data) + sys.getsizeof(start) + sys.getsizeof(end) + 64
    print(f"{description} - Time taken: {end - start:.6f} seconds, Space used: {space_complexity} bytes")
    #print(f"Time Complexity: {time_complexity}\n")

if __name__ == "__main__":
    while True:
        print("1. Insert\n2. Update\n3. Remove\n4. Search\n5. Sort\n6. Best case sort\n7. Worst case sort\n8. EXIT")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            item = Products(int(input("Enter the ID: ")),str(input("Enter the name: ")), float(input("Enter the price: ")), str(input("Enter the category: ")))
            Items.append(item)
            print(f"{item.id} {item.name} {item.price} {item.category} has been inserted")
            
        elif choice == 2:
            i = int(input("Which product are you updating? (Enter the product's ID number)\n"))
            for item in Items:
                if(item.id == i):
                    print(item.id)
                    print(item.name)
                    print(item.price)
                    print(item.category)
                    updated_data = int(input("What would you like to update?\n1. ID\n2. Name\n3. Price \n4. Category\n"))
                    if(updated_data == 1):
                        new_id = input("Enter the new ID: ")
                        item.id = int(new_id)
                        print(f"Succesfully updated to {item.id}")
                    elif(updated_data == 2):
                        new_name = input("Enter the new name: ")
                        item.name = new_name
                        print(f"Successfully updated to {item.name}")
                    elif(updated_data == 3):
                        new_price = input("Enter the new price: ")
                        item.price = float(new_price) 
                        print(f"Successfully updated to {item.price}")   
                    elif(updated_data == 4):
                        new_category = input("Enter the new category: ")
                        item.category = (new_category)
                        print(f"Successfully updated to {item.category}") 
                    else:
                        print("Returning to main menu")
                        break
            
        elif choice == 3:
            i = int(input("Which product would you like to remove? (Enter the product's ID number)\n"))
            for item in Items:
                if(item.id == i):
                    print(f"Successfully removed {item.id} {item.name} {item.price} {item.category}")
                    Items.remove(item)
                    
        elif choice == 4:
            found = False
            i = int(input("Enter the product's ID number\n"))
            for item in Items:
                if(item.id == i):
                    print(item.id)
                    print(item.name)
                    print(item.price)
                    print(item.category)
                    found = True
                    break
            if found:
                print ("Item found")
            else:
                print ("Item not found")
                    
        elif choice == 5:
            analyzeSortPerformance(Items, "Original Data", "O(n^2)")
            #for item in Items:
                #print(item.id, item.name, item.price, item.category)
            
        elif choice == 6:
            data_best = Items.copy()
            analyzeSortPerformance(data_best, "Best Case (Sorted)", "O(n)")
            
        elif choice == 7:
            data_worst = data_best[::-1]
            analyzeSortPerformance(data_worst, "Worst Case (Reverse Sorted)", "O(n^2)")


        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

# Original Data
#data_original = [5, 2, 9, 1, 5, 6, 8, 3, 4, 7]

# Best Case (Already Sorted)
#data_best = sorted(data_original)
#data_best = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

# Average Case (Manually Shuffled)
#data_avg = [3, 7, 4, 6, 5, 2, 8, 1, 9, 5]

# Worst Case (Reverse Sorted)
#data_worst = sorted(data_original, reverse=True)
#data_worst = [9, 8, 7, 6, 5, 5, 4, 3, 2, 1]

#analyzeSortPerformance(Items, "Original Data", "O(n^2)")
#analyzeSortPerformance(data_best, "Best Case (Sorted)", "O(n)")
#analyzeSortPerformance(data_avg, "Average Case (Manually Shuffled)", "O(n^2)")
#analyzeSortPerformance(data_worst, "Worst Case (Reverse Sorted)", "O(n^2)")