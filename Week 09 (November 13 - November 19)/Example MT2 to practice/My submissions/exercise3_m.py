def total_distance(dist, cities):
    total = 0
    if cities == [] or len(cities) == 1:
        return 0
    else:
        for i in range(len(cities) - 1):
            found_connection = False
            for keys in dist.keys():   
                if (cities[i], cities[i + 1]) == keys or (cities[i + 1], cities[i]) == keys:
                    total += dist[keys]
                    found_connection = True
                    break
            if not found_connection:
                return -1
        return total