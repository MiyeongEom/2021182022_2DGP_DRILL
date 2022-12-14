# game world : 객체들의 집합, 리스트로 표현 가능
# 게임 객체 툴이다 !!, 리스트 말하는 거임


objects = [[], [], []]  #2d에선 그리는 순서가 중요함 -> 이중리스트

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()