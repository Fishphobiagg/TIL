TC = int(input())
for i in range(TC):
    n, k = map(int, input().split())
    planet = list(map(int, input().split()))
    planet = sorted(planet)
    spaceship = k
    mobil_count = 0
    for idx, population in enumerate(sorted(planet)):
        if spaceship == population:
            spaceship += population
            planet.remove(population)
            mobil_count += 1
        elif spaceship < population:
            planet.insert(idx, spaceship)
            spaceship_idx = idx
            break
        elif spaceship > population:
            pass

    while True:
        planet[spaceship_idx] += planet[spaceship_idx-1]
        mobil_count += 1
        planet.remove(planet[spaceship_idx-1])
        spaceship_idx -= 1

        while planet[spaceship_idx+1] and planet[spaceship_idx] > planet[spaceship_idx+1]:
            planet[spaceship_idx], planet[spaceship_idx+1] = planet[spaceship_idx+1], planet[spaceship_idx]
            spaceship_idx +=1
        if planet[len(planet)-1] == planet[spaceship_idx] and sum(planet[:spaceship_idx]) <= planet[spaceship_idx]:
            print(f'#{i+1} {mobil_count}')
            break
        else:
            print(f'#{i+1} -1')
