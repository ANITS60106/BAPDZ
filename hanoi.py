def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Переместить диск 1 с {source} на {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Переместить диск {n} с {source} на {target}")
    hanoi(n - 1, auxiliary, target, source)

num_disks = int(input('Write your number: '))
hanoi(num_disks, 'A', 'C', 'B')
