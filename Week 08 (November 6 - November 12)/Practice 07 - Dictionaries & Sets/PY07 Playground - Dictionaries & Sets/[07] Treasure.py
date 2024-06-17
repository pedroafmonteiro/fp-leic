def treasure(clues):
    current_location = (0, 0)
    visited_locations = set()

    while current_location in clues:
        visited_locations.add(current_location)
        current_location = clues[current_location]
        if current_location in visited_locations:
            break

    return current_location