def selectionsort(ls):
    for i in range(len(ls)-1):
        min_pos = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_pos]:
                min_pos = j
        temp = ls[i]
        ls[i] = ls[min_pos]
        ls[min_pos] = temp

aa = [5, 7, 8 , 9, 1, 3, 2, 4]
selectionsort(aa)
print(aa)