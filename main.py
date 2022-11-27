try:
    start = int(input("Ведіть перше число --->"))
    end = int(input("Ведіть друге число --->"))
    while start < end:
        if (start % 5)==0:
            if (start % 3) == 0:
                print(f"Fizz Buzz{start}")
                start += 1
        if (start % 3)==0:
            print(f"Fizz{start}")
            start += 1
        if (start % 5)==0:
            print(f"Buzz{start}")
            start += 1
        if start % 5 and start % 3 == 1:
            print(start)
            start += 1
        if start % 5 and start % 3 == 2:
            print(start)
            start += 1
except Exception as e:
        print(f"Error --> {e}")


