
def bubble_sort(list_to_sort:list[int]):
    for outer_index in range(0, len(list_to_sort) - 1):
        
        has_made_changes = False
        
        for index in range(0, len(list_to_sort) - 1 - outer_index):
            
            current_number = list_to_sort[index]
            next_number = list_to_sort[index + 1]
            
            print(f"Iteration: {outer_index},{index}. Current number: {current_number}, next number: {next_number}.")
            
            if current_number > next_number:
                print("Switching numbers...!!!")
                list_to_sort[index] = next_number
                list_to_sort[index + 1] = current_number
                has_made_changes = True
            
        if not has_made_changes:
            return

list_to_sort = [90,-47,1,6,-3,300,-6]
bubble_sort(list_to_sort)
print(list_to_sort)