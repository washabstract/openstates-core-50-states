import os
import json
import datetime
from pupa.core import db
from pupa.models import Organization
from pupa.models.utils import DatetimeValidator
from pupa.models.schemas.jurisdiction import schema as jurisdiction_schema


def import_jurisdiction(org_importer, jurisdiction):
    jurisdiction = jurisdiction.get_metadata()

    jurisdiction['_type'] = 'jurisdiction'
    jurisdiction['_id'] = jurisdiction.jurisdiction_id
    jurisdiction['latest_update'] = datetime.datetime.utcnow()

    # validate jurisdiction
    validator = DatetimeValidator()
    try:
        validator.validate(jurisdiction, jurisdiction_schema)
    except ValueError as ve:
        raise ve

    db.jurisdictions.save(jurisdiction)

    # create organization(s) (TODO: if there are multiple chambers this isn't right)
    org = Organization(name=jurisdiction['name'], classification='legislature',
                       jurisdiction_id=jurisdiction.jurisdiction_id)
    if 'other_names' in jurisdiction:
        org.other_names = jurisdiction['other_names']
    if 'parent_id' in jurisdiction:
        org.parent_id = jurisdiction['parent_id']

    org_importer.import_object(org)

    # create parties
    for party in jurisdiction['parties']:
        org = Organization(**{'classification': 'party',
                              'name': party['name'],
                              'parent_id': None})
        org_importer.import_object(org)
