import requests
import osm_pb2

def fetch_osm(city):
    # to test multipolygon your can fetch Hamburg as an example. Just uncomment this request for that
    # res = requests.get('https://nominatim.openstreetmap.org/search', params = {
    #     'state': 'Hamburg',
    #     'country': 'germany',
    #     'format': 'geojson',
    #     'polygon_geojson': 1
    # })

    res = requests.get('https://nominatim.openstreetmap.org/search', params = {
        'county': city,
        'country': 'germany',
        'format': 'geojson',
        'polygon_geojson': 1
    })

    return res.json() 


def res_geometry_to_pbf(geometry):
    # check if city has multipolygon like Hamburg
    
    geom_arr = []

    if geometry['type'] == 'Polygon':
        
        n_geometry = osm_pb2.NominatimGeometry()
        n_geometry.type = geometry['type']


        for geom in geometry['coordinates']:
            for sub_geom in geom:
                coordinate = osm_pb2.NominatimCoordinates()
                coordinate.lat = sub_geom[1]
                coordinate.lon = sub_geom[0]
                n_geometry.coordinates.extend([coordinate])

        geom_arr.append(n_geometry)

        return geom_arr

    elif geometry['type'] == 'MultiPolygon':
        
        n_geometry = osm_pb2.NominatimGeometry()
        n_geometry.type = geometry['type']

        for geom in geometry['coordinates']:
            for sub_geom in geom:
                for entry_geom in sub_geom:
                    coordinate = osm_pb2.NominatimCoordinates()
                    coordinate.lat = entry_geom[1]
                    coordinate.lon = entry_geom[0]
                    n_geometry.coordinates.extend([coordinate])
            geom_arr.append(n_geometry)

        return geom_arr
    else:
        return osm_pb2.NominatimGeometry()

def res_json_to_pbf(res_json):
    n_entry = osm_pb2.Nominatim()

    # get the first entry from nominatim response
    feature = res_json['features'][0]

    # map nominatim properties
    n_entry.type = feature['type']
    n_entry.properties.placeId = feature['properties']['place_id']
    n_entry.properties.osmId = feature['properties']['osm_id']
    n_entry.properties.displayName = feature['properties']['display_name']
    n_entry.properties.placeRank = feature['properties']['place_rank']
    n_entry.properties.category = feature['properties']['category']
    n_entry.properties.type = feature['properties']['type']
    n_entry.properties.osmType = feature['properties']['osm_type']

    # map nominatim bounding box
    n_entry.bbox.entry.extend(feature['bbox'])

    # map nominatim geometry
    n_entry.geometry.extend(res_geometry_to_pbf(feature['geometry']))
    return n_entry

def pbf_to_disk(pbf):
    with open ('./nominatim.pbf', 'wb+') as pbf_out:
        pbf_out.write(pbf)

if __name__ == '__main__':
    res_json = fetch_osm('essen')
    pbf = res_json_to_pbf(res_json)
    pbf_to_disk(pbf.SerializeToString(True))
    print(pbf)
   

