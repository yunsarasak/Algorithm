class Vertical_Maneuvering_Equipment:
    def __init__(self, _id, _gass):
        self.id = _id
        self.gasRemain = _gass

n = int(input())

VMEList = []

for i in range(n):
    inputId, inputGas = input().split()
    inputId = int(inputId)
    inputGas = int(inputGas)
    VMEList.append(Vertical_Maneuvering_Equipment(inputId, inputGas))

VMEList.sort(key= lambda VME: VME.id)

for i in range(n):
    print(VMEList[i].id, end=" ")
    print(VMEList[i].gasRemain)
    

