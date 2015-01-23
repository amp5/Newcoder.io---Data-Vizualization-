import geojson

import parse as p

def create_map(data_file):
    """Creates a GeoJSON file."""

    # Define type of GeoJSON that we're creating
    geo_map = {"type": "FeatureCollection"}

    # Define an empty list to collect each point to graph
    item_list = []

    # Iterate over our data to create GeoJSON document (list of points)
    for index, line in enumerate(data_file):
        if line['X'] == "0" or line['Y'] == "0":
            continue   # tells python to skip

        data = {}
        data['type'] = 'Feature'
        data['id'] = index
        data['properties'] = {'title': line['Category'],
                             'description': line['Descript],
                             'date': line['Date'],
                             'location': line['Location']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line["X"], line["Y"])}

        item_list.append(data)

    # Iterate over each point and add to GeoJSON object
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    # Write to a file (GeoJSON)
    with open("file_sf.geojson", "w") as f:
        f.write(geojson.dump(geo_map))


def main():
    data = p.parse(p.MY_FILE, ",")

    return create_map(data)

if __name__ == '__main__':
    main()