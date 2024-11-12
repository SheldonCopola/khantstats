def main():
    try:
        print("\033[32m1. less than x\033[31m")
        
        choice=input("\033[32m please choose\033[0m ")

        mean=float(input("\033[31m penis  \033[0m "))
        std=float(input("\033[31m penis  \033[0m "))
        xxx=float(input("\033[31m penis  \033[0m "))
        why=float(input("\033[31m penis  \033[0m "))
        
        steps=0
        result_m=0
        if choice=='1':
            result_m=mean
            for i in range(5):
                result_m-=std
                steps+=1
                if result_m==xxx:
                    if steps==1:
                        print("84")
                    elif steps==2:
                        print("97.5")

    except ValueError:
        print("kill yourself")
if __name__== "__main__":
    main()