def sort(array: list[int]):
    for next in range(1, len(array), 1):
        curr = next
        temp = array[curr]
        while curr > 0 and temp < array[curr-1]:
            array[curr] = array[curr-1]
            curr-=1
        array[curr] = temp
        yield list(array)