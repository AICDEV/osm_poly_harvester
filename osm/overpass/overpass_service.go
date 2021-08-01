package overpass

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"strconv"
	"strings"
	"time"

	pb "github.com/aicdev/osm_poly_harvester/osm/proto"
)

type overpassService struct {
	QueryFragements     []string
	AreaPolyString      string
	Templates           []string
	OverpassResponse    map[string]interface{}
	OverpassResponseArr []map[string]interface{}
}

type OverpassServiceInterface interface {
	Init()
	FetchOSMData()
	GetOverpassResponse() []map[string]interface{}
}

func NewOverpassService(area []*pb.NominatimGeometry) OverpassServiceInterface {
	return &overpassService{
		QueryFragements: []string{
			"way[\"leisure\"=\"park\"](poly: \"%s\");",
			"way[\"leisure\"=\"forest\"](poly: \"%s\");",
			"way[\"landuse\"=\"meadow\"](poly: \"%s\");",
			"rel[\"leisure\"=\"park\"](poly: \"%s\");",
			"rel[\"leisure\"=\"nature_reserve\"](poly: \"%s\");",
			"rel[\"landuse\"=\"forest\"](poly: \"%s\");",
		},
		AreaPolyString: parseAreaCoordinatesToOSMPoly(area),
	}
}

func (os *overpassService) Init() {
	os.Templates = make([]string, 0)
	for _, v := range os.QueryFragements {
		rawTpl := `
		[out:json];
		(
			` + fmt.Sprintf(v, os.AreaPolyString) + `
		);
		out body geom;
		>;
		out skel geom;
		`
		os.Templates = append(os.Templates, rawTpl)
	}
}

/*******************************************************************
* fetch data from api/interpreter
*******************************************************************/
func (os *overpassService) FetchOSMData() {
	for _, v := range os.Templates {

		data := url.Values{}
		data.Set("data", v)

		req, _ := http.NewRequest("POST", "https://overpass-api.de/api/interpreter", strings.NewReader(data.Encode()))

		req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
		req.Header.Add("Content-Length", strconv.Itoa(len(data.Encode())))

		client := &http.Client{
			Timeout: 180 * time.Second,
		}
		res, err := client.Do(req)

		if err != nil {
			log.Printf("error from osm: %s", err.Error())
		}

		defer res.Body.Close()

		body, err := ioutil.ReadAll(res.Body)

		if err != nil {
			log.Fatal(err.Error())
		} else {
			ovr := os.OverpassResponse
			json.Unmarshal(body, &ovr)
			os.OverpassResponseArr = append(os.OverpassResponseArr, ovr)
		}

	}
}

func (os *overpassService) GetOverpassResponse() []map[string]interface{} {
	return os.OverpassResponseArr
}

func parseAreaCoordinatesToOSMPoly(area []*pb.NominatimGeometry) string {
	parsedCoordinates := ""
	for _, c := range area {
		for i, v := range c.GetCoordinates() {
			if i == len(c.GetCoordinates())-1 {
				parsedCoordinates += fmt.Sprintf("%f %f", v.GetLat(), v.GetLon())
			} else {
				parsedCoordinates += fmt.Sprintf("%f %f ", v.GetLat(), v.GetLon())
			}
		}
	}

	return parsedCoordinates
}
