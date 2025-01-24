from fastapi import APIRouter, Depends

from vkstarter.ai import AICreator, AIUpdater
from vkstarter.ai.deepseek import DeepSeekModel
from vkstarter.db import get_session
from vkstarter.model.atom import PatientAtom
from vkstarter.model.handler import PatientHandler
from vkstarter.model.tree import PatientLeftTree

router = APIRouter(
    prefix = '/note',
    dependencies = [Depends(get_session)]
)

router.add_api_route(
    path = '/patient',
    methods = ['POST'],
    endpoint = AICreator(
        DeepSeekModel,
        lambda note:
            f'''
            Read the following note from a doctor about a new patient and create a new "PatientTree".
            Note: {note}.
            ''',
        PatientLeftTree,
        PatientHandler
    ),
    response_model = PatientAtom
)

router.add_api_route(
    path = '/patient/{id}',
    methods = ['PUT'],
    endpoint = AIUpdater(
        DeepSeekModel,
        lambda record, note:
            f'''
            See the existing record and the following note from a doctor and update the record with a new "PatientTree".

            Record: {record}
            Note: {note}
            ''',
        PatientLeftTree,
        PatientHandler
    )
)
