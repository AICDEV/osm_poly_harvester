package main

import (
	"fmt"
	"io/ioutil"
	"log"

	"github.com/aicdev/osm_poly_harvester/osm/app"
	"github.com/aicdev/osm_poly_harvester/osm/overpass"
	pb "github.com/aicdev/osm_poly_harvester/osm/proto"
	"google.golang.org/protobuf/proto"
)

func main() {
	app.StartApplication()

	/******************************************************************
	* read the nominatim.pbf from ../nominatim/nominatim.pbf
	* and parse the content to our pb struct
	*******************************************************************/

	in, err := ioutil.ReadFile("../nominatim/nominatim.pbf")
	if err != nil {
		log.Fatalln("Error reading file:", err)
	}

	nominatim := &pb.Nominatim{}
	if err := proto.Unmarshal(in, nominatim); err != nil {
		log.Fatalln("Failed to parse nominatim:", err)
	}

	log.Printf("successfully deserialized nominatim pbf for: %s", nominatim.GetProperties().GetDisplayName())

	overpassService := overpass.NewOverpassService(nominatim.GetGeometry())
	overpassService.Init()
	overpassService.FetchOSMData()

	for _, ovr := range overpassService.GetOverpassResponse() {
		fmt.Println(ovr)
	}
}
