def fields(field_):
    # горизонтальное отражение
    def horizontal_reflection(arr):
        return [i[::-1] for i in arr]

    # вертикальное отражение
    def vertical_reflection(arr):
        return arr[::-1]

    # транспонирование
    def transposition(arr):
        arr1 = []
        for _ in range(len(arr)):
            arr1.append('')
        for i in arr:
            for j in range(len(i)):
                arr1[j] += i[j]
        return arr1

    # отражение вдоль горизонтали и вертикали одновременно
    def horizontal_and_vertical_reflection(arr):
        return horizontal_reflection(vertical_reflection(arr))

    # горизонтальное отражение, затем транспонирование
    def horizontal_reflection_and_transposition(arr):
        return transposition(horizontal_reflection(arr))

    # вертикальное отражение, затем транспонирование
    def vertical_reflection_and_transposition(arr):
        return transposition(vertical_reflection(arr))

    # транспонирование, затем два отражения
    def transposition_and_vertical_reflection_and_horizontal_reflection(arr):
        return horizontal_reflection(vertical_reflection(transposition(arr)))

    print()
    print('(исходное поле)')
    print(*field_, sep='\n')

    print()
    print('(горизонтальное отражение)')
    print(*horizontal_reflection(field_), sep='\n')

    print()
    print('(вертикальное отражение)')
    print(*vertical_reflection(field_), sep='\n')

    print()
    print('(транспонирование)')
    print(*transposition(field_), sep='\n')

    print()
    print('(отражение вдоль горизонтали и вертикали одновременно)')
    print(*horizontal_and_vertical_reflection(field_), sep='\n')

    print()
    print('(горизонтальное отражение, затем транспонирование или транспонирование, затем вертикальное отражение)')
    print(*horizontal_reflection_and_transposition(field_), sep='\n')

    print()
    print('(вертикальное отражение, затем транспонирование или транспонирование, затем горизонтальное отражение)')
    print(*vertical_reflection_and_transposition(field_), sep='\n')

    print()
    print('(транспонирование, затем два отражения или два отражения, затем транспонирование) ')
    print(*(transposition_and_vertical_reflection_and_horizontal_reflection(field_)), sep='\n')


s = input()
field = [input() for _ in range(len(s) - 1)]
field.insert(0, s)
fields(field)
