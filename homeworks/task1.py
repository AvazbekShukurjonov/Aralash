def toDrict(*strings):
    dirc = {}
    for i, string in enumerate(strings):
        dirc[f'{i}'] = string
    return dirc


print(toDrict('Hello', 'salom', 'malik'))