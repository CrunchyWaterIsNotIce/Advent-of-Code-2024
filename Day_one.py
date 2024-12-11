
t = 0

def merge_sort(l):
    if len(l) <= 1:
        return l
    else:
        mid = (len(l) - 1) // 2
        left = merge_sort(l[:mid])
        right = merge_sort(l[mid:])
        return merge(left, right)
def merge(left, right):
    out = []
    
    i = 0
    j = 0
    
    
    

with open("Day_one_input.txt") as file:
    data = file.readlines()
    left = []
    right = []
    for line in data:
        nums = line.strip().split("   ")
        left.append(int(nums[0]))
        right.append(int(nums[1]))
        
    left = merge_sort(left)
    right = merge_sort(right)
    
    

print(f"Total distance is : {t}")
        