from sort_visualizer import SortVisualizer

def main():
    loop = True
    while(loop):
        print("Wybierz algorytm (1-4):")
        print("1. Insertion sort")
        print("2. Selection sort")
        print("3. Merge sort")
        print("4. Quick sort")
        alg = input()

        try:
            alg = int(alg)
            if alg not in [1,2,3,4]:
                raise Exception()
        except:
            print("Podaj liczbę od 1 do 4.")
            continue
        
        sv = SortVisualizer(alg)
        sv.start()
        loop = False

if __name__ == '__main__':
    main()