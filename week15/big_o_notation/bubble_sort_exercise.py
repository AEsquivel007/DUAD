
def bubble_sort(list_to_sort:list[int]): # -> The algorithm is: O(n^2).
    for outer_index in range(0, len(list_to_sort) - 1): # O(n)
        
        has_made_changes = False # O(1)
        
        for index in range(0, len(list_to_sort) - 1 - outer_index): # O(n^2)
            
            current_number = list_to_sort[index] # O(1)
            next_number = list_to_sort[index + 1] # O(1)
            
            print(f"Iteration: {outer_index},{index}. Current number: {current_number}, next number: {next_number}.") # O(1)
            
            if current_number > next_number: # O(1)
                print("Switching numbers...!!!") # O(1)
                list_to_sort[index] = next_number # O(1)
                list_to_sort[index + 1] = current_number # O(1)
                has_made_changes = True # O(1)
            
        if not has_made_changes: # O(1)
            return # O(1)

list_to_sort = [90,-47,1,6,-3,300,-6] # O(1)
bubble_sort(list_to_sort) # O(1)
print(list_to_sort) # O(1)