def ArrayChallenge(arr):
    i=0
    cn_digit=0
    cnt = 0
    l = []
    for temp in arr:
        temp = arr[i]
        if temp == arr[i+1]:

            l.append(temp)
            cnt += 1
        else:
            i += 1
    print(l[0])




arr = [1,1, 2, 4, 4, 5,5,5]

print(arr)

ArrayChallenge(arr)