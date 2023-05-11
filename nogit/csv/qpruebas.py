from ast import Mult
from typing import Tuple
from queries import get_all_natural_person_enterprise_by_natural_person_id
#from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.orm.exc import MultipleResultsFound
MULTIPLE_RESULTS_FOUND_EXCEPTION = "Multiple rows were found when one or none was required"
enterprise_id = 15
try:
    natural_person_enterprise = get_all_natural_person_enterprise_by_natural_person_id(197144)
except MultipleResultsFound as e:
    print(e)
    print("lo caché")





""" if natural_person_enterprise and natural_person_enterprise.enterprise_id != enterprise_id:
    print("CACHÉ EL OTRO ERROR")
print(natural_person_enterprise)
print(natural_person_enterprise.natural_person.user.id) """