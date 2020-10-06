def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting('zaki'))
print(greeting(123)) # エラー (greeting()コール時でなく、その中の + による文字結合で)
