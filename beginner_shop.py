item=input("What you wont to buy (computer/laptop/mobile)")

if item =="computer":
    print(f"you need {item}")
    company=input("Which company computer would you like to buy? \n here are some suggested names: (hp/dell/accer/)")
    if company =="hp":
        print(f"Ok you need {item} of {company} company")
        ram=input("how much ram you need in your computer?\n here are some suggested ram's: (4GB/8GB/12GB/)")
        if ram =="4GB":
            price =25000
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram =="8GB":
            price =35000
            print(f"for your required {item} of {company} company price is {price} Rs ")
        else:
            price = 38000
            print(f"for your required {item} of {company} company price is {price} Rs")

    elif  company =="dell":
        print(f"Ok you need {item} of {company} company")
        ram=input("how much ram you need in your computer?\n here are some suggested ram's: (4GB/8GB/12GB/)")
        if ram =="4GB":
            price =50000
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram =="8GB":
            price =48000
            print(f"for your required {item} of {company} company price is {price} Rs")
        else:
            price = 56000
            print(f"for your required {item} of {company} company price is {price} Rs")
    elif company =="accer":
        print(f"Ok you need {item} of {company} company")
        ram=input("how much ram you need in your computer?\n here are some suggested ram's: (4GB/8GB/12GB/)")
        if ram =="4GB":
            price =80000
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram =="8GB":
            price =85000
            print(f"for your required {item} of {company} company price is {price} Rs")
        else:
            price = 90000
            print(f"for your required {item} of {company} company price is {price} Rs")

elif item =="laptop":
    print(f"you need {item}")
    company=input("Which company laptop would you like to buy? \n here are some suggested names: (apple/thinkpad/dell/)")
    if company =="apple":
        print(f"Ok you need {item} of {company} company")
        ram=input("how much ram you need in your laptop?\n here are some suggested ram's: (16GB/32GB/64GB/)")
        if ram =="16GB":
            price =42000
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram =="32GB":
            price =55000
            print(f"for your required {item} of {company} company price is {price} Rs")
        else:
            price = 60000
            print(f"for your required {item} of {company} company price is {price} Rs")

    elif  company =="thinkpad":
        print(f"Ok you need {item} of {company} company")
        ram=input("how much ram you need in your laptop?\n here are some suggested ram's:(16GB/32GB/64GB/)")
        if ram =="16GB":
            price =42000
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram =="32GB":
            price =47000
            print(f"for your required {item} of {company} company price is {price} Rs")
        else:
            price = 47900
            print(f"for your required {item} of {company} company price is {price} Rs")
    elif company =="dell":
        print(f"Ok you need {item} of {company} company")
        ram=input("how much ram you need in your laptop?\n here are some suggested ram's: (16GB/32GB/64GB/)")
        if ram =="16GB":
            price =56000
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram =="32GB":
            price =58600
            print(f"for your required {item} of {company} company price is {price} Rs")
        else:
            price = 51000
            print(f"for your required {item} of {company} company price is {price} Rs")

else:
    print(f"you need {item}")
    company = input("Which company mobile would you like to buy? \n here are some suggested names: (iphone/infinix/sumsang/)")
    if company == "iphone":
        print(f"Ok you need {item} of {company} company")
        ram = input("how much ram you need in your mobile?\n here are some suggested ram's: (32GB/64GB/128GB/)")
        if ram == "32GB":
            price = 60000
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram == "64GB":
            price = 70000
            print(f"for your required {item} of {company} company price is {price} Rs")
        else:
            price = 75000
            print(f"for your required {item} of {company} company price is {price} Rs")

    elif company == "infinix":
        print(f"Ok you need {item} of {company} company")
        ram = input("how much ram you need in your mobile?\n here are some suggested ram's: (32GB/64GB/128GB/)")
        if ram == "32GB":
            price = 25000
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram == "64GB":
            price = 30000
            print(f"for your required {item} of {company} company price is {price} Rs")
        else:
            price = 35000
            print(f"for your required {item} of {company} company price is {price} Rs")
    elif company == "sumsang":
        print(f"Ok you need {item} of {company} company")
        ram = input("how much ram you need in your mobile?\n here are some suggested ram's:  (32GB/64GB/128GB/)")
        if ram == "32GB":
            price = 52500
            print(f"for your required {item} of {company} company price is {price} Rs")
        elif ram == "64GB":
            price = 70000
            print(f"for your required {item} of {company} company price is {price} Rs")
        else:
            price = 95000
            print(f"for your required {item} of {company} company price is {price} Rs")



