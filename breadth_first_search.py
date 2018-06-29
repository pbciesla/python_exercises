from collections import deque


def check_condition(element):
    return 'dog' in element


def search(element):
    searched = []
    search_queue = deque()
    search_queue += graph[element]

    while search_queue:
        obj = search_queue.popleft()
        if obj not in searched:
            if check_condition(obj):
                print('{} is a dog!'.format(obj))
                return True
            else:
                if obj in graph.keys():
                    search_queue += graph[obj]
                searched.append(obj)
    return False


graph = {'Wojtek': ['Zosia', 'Kuba', 'Miki mouse'],
         'Zosia': ['Marta', 'Puszek cat'],
         'Bartek': ['Filip', 'Czarek'],
         'Filip': ['Ula fish', 'Mordka cat'],
         'Marta': ['Lolek rat', 'Bartek'],
         'Czarek': ['Reksio dog', 'Stefan']}

search('Wojtek')
