##create parent class
class Building:
    address = ''
    sq_ft = 0
    lease_terms = ''
    rent_cost = ''


##create child class from parent
class Residential(Building):
    tentant_names: ''
    number_tenants: 0
    number_pets: 0

##create child class from parent
class Commercial(Building):
    business_type: ''
    
    
    
