start = int(input("Ведіть перше число --->"))
end = int(input("Ведіть друге число --->"))
while start < end:
    if int(start % 7)==0:
        print(f"Number {start} is multiple 7")
    start += 1
