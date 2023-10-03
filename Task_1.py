import requests

def most_intelligence(hero_list):
    all_heroes_list = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
 
    intel_list = []
    for item in all_heroes_list:
        name = item['name'] 
        if name in hero_list:
       
            intel = item['powerstats']['intelligence']
            intel_list.append([intel, name])

    intel_list.sort(reverse=True)

    print(f'Самый умный герой {intel_list[0][1]}')

most_intelligence(['Hulk', 'Captain America', 'Thanos'])