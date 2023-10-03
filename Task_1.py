import requests

def most_intelligence(hero_list):
    all_heroes_list = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
    all_heroes_list_tuples = []
    for item in all_heroes_list:
        hero_tuple = list(item.items())
        all_heroes_list_tuples.append(hero_tuple)
    
    intel_list = []
    for hero in hero_list:
        for item in all_heroes_list_tuples:
            name = item[1][1]
            intel = list(item[3])[1]['intelligence']
            
            if name == hero:
                intel_list.append([name, intel])

    def int_key(l):
        return l[1]

    intel_list.sort(key=int_key, reverse=True)

    print(f'Самый умный герой {intel_list[0][0]}')

most_intelligence(['Hulk', 'Captain America', 'Thanos'])