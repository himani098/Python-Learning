def main():
    hello()
    name = input("Enter your name: ")
    hello(name)
 
def hello(name = "everyone"):
    print("Hello,",name)

main()
