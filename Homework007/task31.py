# values = [0,2,10,6]
# same_by = lambda x: x%2, values
# if same_by(lambda x: x%2, values):
#     print('same')
# else:
#     print('different')
def same_by(characteristic, objects):
    if not objects:
        return True
    etalon = characteristic(objects[0])
    for i in objects:
        if characteristic(i) != etalon:
            return False
    return True


values = [1, 2, 3, 4]
print(same_by(lambda x: x % 2, values))
