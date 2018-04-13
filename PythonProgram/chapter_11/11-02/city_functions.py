def get_formatted_city(city_name, country_name, population=None):
    if population:
        formatted = city_name.title() + ', ' + country_name.title() + \
            ' - population ' + str(population)
    else:
        formatted = city_name.title() + ', ' + country_name.title()
    return formatted
