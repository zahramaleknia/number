def t_s_n():
    try:
        num=int(input("enter number"))
        while num>=10:
            num=sum(int(digit)for digit in str(num))
        print(f"your number:{num}")
    except ValueError:
        print("enter a number{num}")
t_s_n()