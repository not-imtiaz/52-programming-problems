import sys

def main():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
        
        for _ in range(n):
            num = sys.stdin.readline().strip()
            if not num:
                print(0)
                continue
            
            words = num.split()
            print(len(words))
    except EOFError:
        pass

if __name__ == "__main__":
    main()