import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(zoznam):
    cisla=zoznam.copy()
    n=len(cisla)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if cisla[j] < cisla[min_idx]:
                min_idx = j

        # Prohodíme nalezené minimum s prvkem na pozici i
        cisla[i], cisla[min_idx] = cisla[min_idx], cisla[i]

    return cisla


def bubble_sort(zoznam):
    n = len(zoznam)
    for i in range(n):
        for j in range(0,n-1):
            if zoznam[j]>zoznam[j+1]:
                zoznam[j], zoznam[j+1]= zoznam[j+1], zoznam[j]
    return zoznam

def main():
    cisla_test=(random_numbers(20))
    print(cisla_test)
    print(selection_sort(cisla_test))
    print(bubble_sort(cisla_test))


if __name__ == '__main__':
   main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
