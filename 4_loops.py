students=["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student.upper())

## Uygulama ##
#before: "hi my name is john and i am learning python"
#after:  "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index%2==0:
            new_string+=string[string_index].upper()
        else:
            new_string+=string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")


### Enumerate ###
# enumerate() fonksiyonu, bir liste üzerinde döngü yaparken hem indeks hem de eleman değerini aynı anda almanıza olanak sağlar.
students=["John", "Mark", "Venessa", "Mariam"]

A=[]
B=[]
for index,student in enumerate(students):
    if index%2==0:
        A.append(student)
    else:
        B.append(student)
print(A)