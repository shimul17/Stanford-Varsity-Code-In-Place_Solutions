# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    human_years = int(input("Enter an age in calendar years: "))  
    dog_years = human_years * DOG_YEARS_MULTIPLIER
    print(f"That's {dog_years} in dog years!")

if __name__ == '__main__':
    main()
