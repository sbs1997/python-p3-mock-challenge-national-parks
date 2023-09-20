class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    # name property
    def get_name(self):
        return self._name
    def set_name(self, input):
        if not hasattr(self, "name"):
            if type(input) == str and len(input)>=3:
                self._name = input
            else:
                raise Exception("Name must be a string between 1 and 15 characters long")
        else:
            raise Exception("The name of parks cannot be changed")
    name = property(get_name, set_name)

    def trips(self):
        park_trips = []
        for trip in Trip.all:
            if trip.national_park == self:
                park_trips.append(trip)
        return park_trips

    def visitors(self):
        park_visitors = []
        for trip in Trip.all:
            if trip.national_park == self and trip.visitor not in park_visitors:
                park_visitors.append(trip.visitor)
        return park_visitors
    
    def total_visits(self):
        visits = 0
        for trip in Trip.all:
            if trip.national_park == self:
                visits +=1
        return visits
        
    
    def best_visitor(self):
        champ = None
        champ_total = 0
        for visitor in Visitor.all:
            if visitor.total_visits_at_park(self) > champ_total:
                champ = visitor
                champ_total = visitor.total_visits_at_park(self)
        return champ
    
    @classmethod
    def most_visited(cls):
        champ = None
        champ_total = 0
        for park in cls.all:
            if park.total_visits()>champ_total:
                champ = park
                champ_total = park.total_visits()
        return champ

class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    # start date property
    def get_start_date(self):
        return self._start_date
    def set_start_date(self, input):
        if type(input) == str and len(input)>=7:
            self._start_date = input
        else:
            raise Exception("Must be a string in the format: September 1st")
    start_date = property(get_start_date, set_start_date)

    # end date property
    def get_end_date(self):
        return self._end_date
    def set_end_date(self, input):
        if type(input) == str and len(input)>=7:
            self._end_date = input
        else:
            raise Exception("Must be a string in the format: September 1st")
    end_date = property(get_end_date, set_end_date)

    # visitor propety
    def get_national_park(self):
        return self._national_park
    def set_national_park(self, input):
        if type(input) == NationalPark:
            self._national_park = input
        else:
            raise TypeError("park must be of the NationalPark type")
        
    
    # park propety
    def get_visitor(self):
        return self._visitor
    def set_visitor(self, input):
        if type(input) == Visitor:
            self._visitor = input
        else:
            raise TypeError("visitor must be of the visitor type")
    

class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    # name property
    def get_name(self):
        return self._name
    def set_name(self, input):
        if type(input) == str and 1<=len(input)<=15:
            self._name = input
        else:
            raise Exception("Name must be a string between 1 and 15 characters long")
    name = property(get_name, set_name)
        
    def trips(self):
        visitor_trips = []
        for trip in Trip.all:
            if trip.visitor == self:
                visitor_trips.append(trip)
        return visitor_trips
    
    def national_parks(self):
        visitor_parks = []
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park not in visitor_parks:
                visitor_parks.append(trip.national_park)
        return visitor_parks
    
    def total_visits_at_park(self, park):
        visits = 0
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park == park:
                visits +=1
        return visits
    
