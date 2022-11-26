try:
    start = int(input("Ведіть перше число --->"))
    num = start
    num1 = start
    num3 = start
    end = int(input("Ведіть друге число --->"))
    num2 = end
    num4 = end
    sum = 0
    while start < end:
        print(start , end=" ")
        start += 1
    print()
    while num < end:
        print(end , end=" ")
        end -= 1
    print()
    while num1 < num2:
        if int(num1 % 7)==0:
            print(f"Number {num1} is multiple 7")
        num1 += 1
    while num3 < num4:
        if int(num3 % 5)==0:
            sum += 1

        num3 += 1
    print(sum)
except Exception as e:
    print(f"Error --> {e}")
