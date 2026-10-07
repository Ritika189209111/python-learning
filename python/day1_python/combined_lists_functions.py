marks = [78, 85, 91, 73, 88]
def calculate_total(marks):
    total = sum(marks)
    return total
def calculate_average(marks):
    average = calculate_total(marks)/len(marks)
    return average 
result = calculate_total(marks)
print(result)
outcome = calculate_average(marks)
print(outcome)

print(len(marks))
print(max(marks))
print(min(marks))

for i in marks:
    if i>=80:
        print(i)
        


        
