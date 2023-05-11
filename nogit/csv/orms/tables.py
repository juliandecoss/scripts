from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, Column, DefaultClause, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime, Date, CHAR
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    DefaultClause,
    Float,
    ForeignKey,
    Integer,
    String,
)
from base_model import KonfioModel
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.schema import Table

class VerificationOtp(KonfioModel):

    __tablename__ = "OTP_VERIFICATION_CODE"

    id = Column(Integer, primary_key=True)
    entity_phone_id = Column(
        Integer,
        DefaultClause("0"),
        ForeignKey("KONFIO.ENTITY_PHONE.id"),
        nullable=False,
    )
    otp_code = Column(String(100), nullable=False)
    valid_time = Column(Integer)
    created_date = Column(DateTime, DefaultClause(func.now()))
    last_updated_date = Column(DateTime, DefaultClause(func.now(), for_update=True))
    is_verified = Column(Integer, DefaultClause("0"))

    #entity_phone = relationship("Phone", foreign_keys=[entity_phone_id])
person_phone_table = Table(
    "NATURAL_PERSON_PHONE",
    KonfioModel.metadata,
    Column("phone_id", Integer, ForeignKey("KONFIO.ENTITY_PHONE.id")),
    Column("natural_person_id", Integer, ForeignKey("KONFIO.NATURAL_PERSON.id")),
    schema="KONFIO",
)
class NaturalPerson(KonfioModel):

    __tablename__ = "NATURAL_PERSON"

    id = Column("id", Integer, primary_key=True)
    email = Column("email", String(255))
    dob = Column("dob", Date)
    gender = Column("gender", Integer)
    rfc = Column(String(13))
    curp = Column("curp", String(18))
    house_phone_number = Column("house_phone_number", String(15))
    mobile_phone_number = Column("mobile_phone_number", String(15))
    name = Column("name", String(255))
    paternal_last_name = Column("paternal_last_name", String(255))
    maternal_last_name = Column("maternal_last_name", String(255))
    place_of_birth_id = Column(
        "place_of_birth",
        Integer,
        ForeignKey("KONFIO.LU_PLACE_OF_BIRTH.PLACE_OF_BIRTH_ID"),
    )
    street = Column("address_street", String(255))
    interior_number = Column("address_interior", String(255))
    neighborhood = Column("address_neighborhood", String(255))
    municipality = Column("address_municipality", String(255))
    municipality_id = Column("address_municipality_id", Integer)
    zip_code = Column("zip_code", String(5))
    city = Column("address_city", String(255))
    created_date = Column("created_date", DateTime, DefaultClause(func.now()))
    updated_date = Column(
        "last_updated_date", DateTime, DefaultClause(func.now(), for_update=True)
    )
    state_id = Column(
        "address_state",
        Integer,
        ForeignKey("KONFIO.LU_PLACE_OF_BIRTH.PLACE_OF_BIRTH_ID"),
    )

    gender = Column("gender", Integer, ForeignKey("KONFIO.LU_GENDER.GENDER_ID"))
    is_tax_exempt = Column("is_tax_exempt", Boolean, DefaultClause("1"), nullable=False)
    user = relationship("User", back_populates="natural_person", uselist=False)
    phones: "RelationshipProperty[List[Phone]]" = relationship(
        "Phone", secondary=person_phone_table
    )
    
"""
    lu_place_of_birth = relationship("LuPlaceOfBirth", foreign_keys=[place_of_birth_id])
    addresses = relationship("Address", secondary=person_address_table)
    bank_accounts = relationship("BankAccount", secondary=person_bank_account_table)
    defendant = relationship("Defendant", secondary=person_defendant_table)"""


class User(KonfioModel):

    __tablename__ = "user"

    id = Column("user_id", Integer, primary_key=True)
    natural_person_id = Column(Integer, ForeignKey("KONFIO.NATURAL_PERSON.id"))
    name = Column("NAME", String(50))
    paternal_last_name = Column("PATERNAL_LAST_NAME", String(50))
    maternal_last_name = Column("MATERNAL_LAST_NAME", String(50))
    dob = Column("DOB", Date)
    email = Column(String(255))
    email_verification = Column("EMAIL_VERIFICATION_DATE", DateTime)
    house_phone_number = Column("HOUSE_NUMBER", String(15))
    mobile_phone_number = Column("MOBILE_NUMBER", String(15))
    password = Column(String(128), DefaultClause(""), nullable=False)
    registration_date = Column("REGISTRATION_DATE", DateTime, DefaultClause(func.now()))
    username = Column("username", String(255))
    registration_week_id = Column("REGISTRATION_WEEK_ID", Integer)
    invoice_to_rfc = Column("INVOICE_TO_RFC", String(50))
    google_source = Column("GOOGLE_SOURCE", String(50))
    google_medium = Column("GOOGLE_MEDIUM", String(20))
    google_campaing = Column("GOOGLE_CAMPAIGN", String(150))
    google_keyword = Column("GOOGLE_KEYWORD", String(150))
    google_device = Column("GOOGLE_DEVICE", String(50))
    gclid = Column("gclid", String(100))
    promo_code = Column("promo_code", Integer)
    uber_type = Column("UBER_TYPE", Integer)
    house_latitude = Column("HOUSE_LATITUDE", Float)
    house_longitude = Column("HOUSE_LONGITUDE", Float)
    fico_band_id = Column("FICO_BAND_ID", Integer)
    user_type = Column("USER_TYPE", Integer)
    status_id = Column(
        "USER_STATUS_ID",
        Integer,
        DefaultClause("1"),
        ForeignKey("KONFIO.LU_USER_STATUS.id"),
        nullable=False,
    )
    street = Column("ADDRESS_STREET", String(100))
    interior_number = Column("ADDRESS_INTERIOR", String(100))
    neighborhood = Column("ADDRESS_NEIGHBORHOOD", String(100))
    municipality = Column("ADDRESS_MUNICIPALITY", String(100))
    municipality_id = Column(
        "ADDRESS_MUNICIPALITY_ID",
        Integer,
        ForeignKey("KONFIO.LU_ZIP_CODE_MUNICIPIO.ZIP_CODE_MUNICIPIO_ID"),
    )
    zip_code = Column("ZIP_CODE", String(5))
    city = Column("ADDRESS_CITY", String(50))
    state_id = Column(
        "ADDRESS_STATE",
        Integer,
        ForeignKey("KONFIO.LU_PLACE_OF_BIRTH.PLACE_OF_BIRTH_ID"),
    )
    place_of_birth_id = Column(
        "PLACE_OF_BIRTH",
        Integer,
        ForeignKey("KONFIO.LU_PLACE_OF_BIRTH.PLACE_OF_BIRTH_ID"),
    )
    gender = Column("GENDER", Integer, ForeignKey("KONFIO.LU_GENDER.GENDER_ID"))
    curp = Column("CURP", String(18))
    rfc = Column("RFC", String(13))
    is_active = Column("state", Boolean, DefaultClause("1"), nullable=False)
    updated_date = Column(
        "LAST_UPDATED_DATE", DateTime, DefaultClause(func.now(), for_update=True)
    )
    natural_person = relationship(
        "NaturalPerson",
        foreign_keys=[natural_person_id],
        back_populates="user",
        uselist=False,
    )


class UserAdmin(KonfioModel):

    __tablename__ = "user_admin"

    id = Column("user_id", Integer, primary_key=True)
    username = Column("username", String(255))
    email = Column("email", String(255))
    display_name = Column("display_name", String(50))
    full_name = Column("full_name", String(255))
    role = Column("role", CHAR(1), DefaultClause("S"), nullable=False)
    curp = Column("curp", String(18))
    password = Column("password", String(128))
    state = Column("state", Boolean)
    mobile_number = Column("MOBILE_NUMBER", Integer)
    date_registered = Column("DATE_REGISTERED", DateTime, DefaultClause(func.now()))
    date_unregistered = Column("DATE_UNREGISTERED", DateTime)
    dob = Column("DOB", Date)
    two_factor_authenticator = Column("two_factor_authenticator", String(16))
    salesforce_id = Column("salesforce_id", String(18))


class SsoUserRelation(KonfioModel):
    __tablename__ = "SSO_RELATION"

    sso_id = Column(String(36), primary_key=True)
    user_id = Column(Integer, ForeignKey("KONFIO.user.user_id"), nullable=True)
    user_admin_id = Column(
        Integer, ForeignKey("KONFIO.user_admin.user_id"), nullable=True
    )
    created_date = Column(DateTime, DefaultClause(func.now()), nullable=False)

    user = relationship(User, foreign_keys=[user_id])
    user_admin = relationship("UserAdmin", foreign_keys=[user_admin_id])


class Phone(KonfioModel):

    __tablename__ = "ENTITY_PHONE"

    id = Column(Integer, primary_key=True)
    country_code = Column(String(10), DefaultClause("+52"), nullable=False)
    number = Column("phone_number", String(15))
    type_id = Column(
        "phone_number_type", Integer, ForeignKey("KONFIO.LU_PHONE.id"), nullable=False
    )
    status_id = Column(
        "phone_number_status", Integer, ForeignKey("KONFIO.LU_PHONE.id"), nullable=False
    )
    source_id = Column("phone_number_source", Integer, ForeignKey("KONFIO.LU_PHONE.id"))
    comments = Column(String(300))
    created_by_id = Column(
        "created_by", Integer, ForeignKey("KONFIO.user_admin.user_id")
    )
    updated_by_id = Column(
        "last_updated_by", Integer, ForeignKey("KONFIO.user_admin.user_id")
    )
    is_primary = Column(Integer, DefaultClause("0"))
    is_active = Column(Integer, DefaultClause("1"))
    created_date = Column(DateTime, DefaultClause(func.now()))
    updated_date = Column(
        "last_updated_date", DateTime, DefaultClause(func.now(), for_update=True)
    )

    """ created_by = relationship("UserAdmin", foreign_keys=[created_by_id])
    updated_by = relationship("UserAdmin", foreign_keys=[updated_by_id])
    type = relationship("LuPhone", foreign_keys=[type_id])
    status = relationship("LuPhone", foreign_keys=[status_id])
    source = relationship("LuPhone", foreign_keys=[source_id]) """


class NaturalPersonEnterprise(KonfioModel):
    __tablename__ = "NATURAL_PERSON_ENTERPRISE"

    id = Column(Integer, primary_key=True)
    natural_person_id = Column(Integer, ForeignKey("KONFIO.NATURAL_PERSON.id"))
    enterprise_id = Column(Integer, ForeignKey("KONFIO.ENTERPRISE.id"), nullable=False)
    role_id = Column(
        Integer, ForeignKey("KONFIO.LU_NATURAL_PERSON_ROLE.id"), nullable=False
    )
    validate_role_start_date = Column(DateTime)
    validate_role_end_date = Column(DateTime)
    created_by_id = Column(
        "created_by", Integer, ForeignKey("KONFIO.user_admin.user_id"), nullable=False
    )
    created_date = Column(DateTime, DefaultClause(func.now()), nullable=False)
    updated_by_id = Column(
        "last_updated_by", Integer, ForeignKey("KONFIO.user_admin.user_id")
    )
    last_updated_date = Column(DateTime, DefaultClause(func.now()), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)
    token_key_path = Column(String(256))
    token_expiration = Column(DateTime)

    enterprise = relationship("Enterprise", foreign_keys=[enterprise_id])
    natural_person = relationship("NaturalPerson", foreign_keys=[natural_person_id])
    """ created_by = relationship("UserAdmin", foreign_keys=[created_by_id])
    updated_by = relationship("UserAdmin", foreign_keys=[updated_by_id])
    enterprise = relationship("Enterprise", foreign_keys=[enterprise_id])
    role = relationship("LuNaturalPersonRole", foreign_keys=[role_id])
    natural_person = relationship("NaturalPerson", foreign_keys=[natural_person_id])
 """


class Enterprise(KonfioModel):
    __tablename__ = "ENTERPRISE"

    id = Column(Integer, primary_key=True)
    rfc = Column(String(13))
    name = Column(String(1000))
    commercial_name = Column(String(150))
    entity_type = Column(
        "type_id", Integer, ForeignKey("KONFIO.LU_ENTITY_TYPE.id"), nullable=False
    )
    is_completed = Column(Boolean, DefaultClause("0"))
    completed_date = Column("is_completed_date", DateTime)
    created_by_id = Column(
        "created_by", Integer, ForeignKey("KONFIO.user_admin.user_id"), nullable=False
    )
    created_date = Column(DateTime, DefaultClause(func.now()), nullable=False)
    updated_by_id = Column(
        "last_updated_by", Integer, ForeignKey("KONFIO.user_admin.user_id")
    )
    last_updated_date = Column(DateTime, DefaultClause(func.now()), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)

    """ created_by = relationship("UserAdmin", foreign_keys=[created_by_id])
    updated_by = relationship("UserAdmin", foreign_keys=[updated_by_id])
    lu_entity_type = relationship("LuEntityType", foreign_keys=[entity_type]) """



class LuNaturalPersonRole(KonfioModel):
    __tablename__ = "LU_NATURAL_PERSON_ROLE"

    id = Column(Integer, primary_key=True)
    description = Column(String(45))
    created_by_id = Column(
        "created_by", Integer, ForeignKey("KONFIO.user_admin.user_id"), nullable=False
    )
    created_date = Column(DateTime, DefaultClause(func.now()), nullable=False)
    updated_by_id = Column(
        "last_updated_by", Integer, ForeignKey("KONFIO.user_admin.user_id")
    )
    last_updated_date = Column(DateTime, DefaultClause(func.now()), nullable=False)
    is_active = Column(Boolean, DefaultClause("1"), nullable=False)

    """ created_by = relationship("UserAdmin", foreign_keys=[created_by_id])
    updated_by = relationship("UserAdmin", foreign_keys=[updated_by_id]) """