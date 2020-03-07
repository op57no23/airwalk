# [Airwalk -- pollution routing: https://morning-reef-21847.herokuapp.com/](https://morning-reef-21847.herokuapp.com/) 

Research has shown that air pollution can vary dramatically within short distances. Airwalk gives users the ability to choose walking and cycling routes based on street level pollution data. The site uses [data from aqdatacommons](https://aqdatacommons.org/superset/dashboard/bay_area_mobile_analysis/), routing from the Google Directions API, rendering from the Mapbox API, and calculating from the Turf js library to score and display routes. Although data is not real-time and only covers certain Bay Area neighborhoods, the site is a proof of concept for similar applications of this type of data.

## The Data

From the aqdatacommons website:

> Mobile monitoring data were collected at 1 Hz and processed as described in Messier et al. (2018, DOI: 10.1021/acs.est.8b03395). The values presented are the median of drive pass means at each 30m road segment.

> Spatial coverage: The data include a set of 10 neighborhoods within the San Francisco Bay Area: Downtown Oakland, West Oakland, East Oakland, Inner Oakland (this is not contiguous but patches within Inner Oakland), Berkeley (not contiguous), San Jose, Santa Clara, Redwood City, Palo Alto, San Francisco Richmond district, Berkeley, and two within surrounding counties: Livermore, Sebastopol.

> Temporal coverage: Median values are based on data collected during a campaign that began on May 28, 2015 and ended December 21, 2017. The first six months of driving included only the four Oakland neighborhoods (Downtown, West, East, and Inner Oakland). Livermore, Berkeley, and SF Richmond were added in Nov/Dec of 2015, and visits to the other neighborhoods began June/July of 2016. After July of 2016, all neighborhoods were visited on a rotating basis until the end of the campaign.

> During the summer of 2017, mobile monitoring focused exclusively on the neighborhood of West Oakland as part of a complementary study. To avoid seasonal bias, data collected during the intensive driving campaign were excluded in calculating the median values presented here.

## How routes are scored

After receiving a route from the Google directions API, the site places points at .2 mile increments along the route. Turf js is used to find the nearest 5 points from the dataset which contribute to the score of the point on the route according to [inverse distance weighting](https://en.wikipedia.org/wiki/Inverse_distance_weighting). The subsequent scores from each point on the route are averaged to give the black carbon value for the entire route.



