value = [('acc1', 1500), ('acc2', 500), ('acc3', 750)]
info = dict(value)
acc = str(input("Input acc name: "))
if acc not in info.keys():
    print("Acc dont exits\n")
else:
    print("Before: ", info.get(acc))
    num = int(input("Input money: "))
    info[acc] += num
    print("After: ", info.get(acc))
print("END!!!")

