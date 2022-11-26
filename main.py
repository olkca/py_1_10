start = int(input("Ведіть перше число --->"))
end = int(input("Ведіть друге число --->"))
while start < end:
    if int(start % 3)==0:
        print("Fizz")
    if int(start % 5)==0:
        print("Buzz")
    if int(start % 5)==0:
        if int(start % 3)==0:
            print("Fizz Buzz")
    if int(start % 5)==1:
        if int(start % 3)==1:
            print(start)
            start += 1
    start += 1

