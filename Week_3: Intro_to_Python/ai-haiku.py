from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print('Creating your haiku....')
    promt = f"Write a haiku about {topic} for a person named {name},"\
    f"The haiku must follow the 5-7-5 syllable structure."
    haiku = call_gpt(promt)
    print("\n" + haiku)
  
if __name__ == "__main__":
    main()
