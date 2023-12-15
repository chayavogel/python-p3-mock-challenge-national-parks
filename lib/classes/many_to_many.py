class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 3 <= len(name) and not hasattr(self, "_name"):
            self._name = name
            return self._name
        
    def trips(self):
        trips = [trip for trip in Trip.all if trip.national_park == self]
        return trips
    
    def visitors(self):
        visitor_set = {trip.visitor for trip in Trip.all if trip.national_park == self}
        visitor_list = list(visitor_set)
        return visitor_list
    
    def total_visits(self):
        visits = [trip for trip in Trip.all if trip.national_park == self]
        return len(visits)
    
    def best_visitor(self):
        List = [trip.visitor for trip in Trip.all if trip.national_park == self]

        counter = 0
        num = List[0]
     
        for i in List:
            curr_frequency = List.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                num = i
    
        return num


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        # make the date the correct format
        if isinstance(start_date, str) and 7 <= len(start_date):
            self._start_date = start_date
        return self._start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        # make the date the correct format
        if isinstance(end_date, str) and 7 <= len(end_date):
            self._end_date = end_date
        return self._end_date
    
    @property
    def visitor(self):
        return self._visitor 
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        return self._visitor
    
    @property
    def national_park(self):
        return self._national_park 
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        return self._national_park

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        return self._name
        
    def trips(self):
        trips = [trip for trip in Trip.all if trip.visitor == self]
        return trips
    
    def national_parks(self):
        national_parks_set = {trip.national_park for trip in Trip.all if trip.visitor == self}
        national_parks_list = list(national_parks_set)
        return national_parks_list
    
    def total_visits_at_park(self, park):
        pass