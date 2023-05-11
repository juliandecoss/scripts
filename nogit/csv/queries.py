from orms.tables import (
    NaturalPerson, 
    SsoUserRelation, 
    User, 
    NaturalPersonEnterprise, 
    Enterprise,
    LuNaturalPersonRole,
    )
from alchemy_db import session

def get_np_id_by_email(email):
    person = session.query(NaturalPerson).filter(NaturalPerson.email == email).first()
    if person: 
        return person
    return None

def get_np_by_id(id):
    return session.query(NaturalPerson).get(id)


def get_user_id_by_email(email=""):
    person = session.query(User).filter(User.email == email).first()
    if person: 
        return person
    return None

def get_sso_relation(email=""):
    user_id = get_user_id_by_email(email)
    sso = session.query(SsoUserRelation).filter(SsoUserRelation.user_id == user_id).all()
    if sso: 
        return sso
    return None

def get_natural_person_enterprise(np_id):
    return (
        session.query(NaturalPersonEnterprise).filter(
            NaturalPersonEnterprise.natural_person_id == np_id,
            NaturalPersonEnterprise.is_active == True,
        ).all()
    )

def get_all_data(np_id):
    return (
        session.query(NaturalPersonEnterprise,Enterprise,LuNaturalPersonRole)
        .filter(NaturalPersonEnterprise.enterprise_id == Enterprise.id)
        .filter(NaturalPersonEnterprise.role_id == LuNaturalPersonRole.id)
        .filter(
            NaturalPersonEnterprise.natural_person_id == np_id,
            NaturalPersonEnterprise.is_active == True,
        ).all()
    )

def get_sso_relation_by_user_id(natural_person_id):
    return (
        session.query(SsoUserRelation,User)
        .join(User, User.id == SsoUserRelation.user_id)
        .filter(User.natural_person_id == natural_person_id)
        .first()
    )

def get_all_natural_person_enterprise_by_natural_person_id(natural_person_id):
    return session.query(NaturalPersonEnterprise).filter_by(natural_person_id=natural_person_id, is_active=True).one_or_none() 


#user = get_user_id_by_email("rcardenast@walook.com.mx")
