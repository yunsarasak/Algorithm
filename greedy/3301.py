n = int(input())
remainingChange = n

#Ž���� ���� �Ӽ��� ���°�?
#�Ž������� ��������
#���� ���� �����ϴ� ���� ������ ( �ּ� �Ž����� )�� �����Ѵ�.

result = 0

while (remainingChange != 0):
    if remainingChange >= 50000:
        remainingChange -= 50000
    elif remainingChange >= 10000:
        remainingChange -= 10000
    elif remainingChange >= 5000:
        remainingChange -= 5000
    elif remainingChange >= 1000:
        remainingChange -= 1000
    elif remainingChange >= 500:
        remainingChange -= 500
    elif remainingChange >= 100:
        remainingChange -= 100 
    elif remainingChange >= 50:
        remainingChange -= 50 
    elif remainingChange >= 10:
        remainingChange -= 10 

    result += 1

print(result)
