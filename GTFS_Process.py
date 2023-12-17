from gtfs_functions import Feed

#pull GTFS
gtfs_path = 'https://www.itsmarta.com/google_transit_feed/google_transit.zip'
feed = Feed(gtfs_path, time_windows=[0, 6, 10, 12, 16, 19, 24])

routes = feed.routes
routes.head(2)

#Find planned trips for current time from GTFS (calendar.txt, trips.txt)

#Pull actual trips  for current time from GTFS-RT (vehiclepositions.pb)

#Compare planned with actual, build DF with missed trips [[trip, route]]

#return table of missed trips