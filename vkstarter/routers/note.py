from fastapi import APIRouter
from sqlalchemy import Engine

from vkstarter.ai import AICreator, AIUpdater
from vkstarter.ai.deepseek import DeepSeekModel
from vkstarter.model.atom import PatientAtom
from vkstarter.model.handler import PatientHandler, VisitHandler
from vkstarter.model.tree import PatientLeftTree, VisitTree


def create_router(engine: Engine) -> APIRouter:
    '''Create the note router.'''
    router = APIRouter(prefix = '/note',)
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
            PatientHandler,
            engine
        ),
        response_model = PatientAtom,
        name = 'AI Patient Creator',
        description = 'Create a new Patient record from a note.'
    )
    router.add_api_route(
        path = '/patient/{id}',
        methods = ['PUT'],
        endpoint = AIUpdater(
            DeepSeekModel,
            lambda record, note:
                f'''
                See the existing record and the following note from a doctor and update the record
                with a new "PatientTree".

                Record: {record}
                Note: {note}
                ''',
            PatientLeftTree,
            PatientHandler,
            engine
        ),
        name = 'AI Patient Updater',
        description = 'Update an exiting Patient record from a note.'
    )
    router.add_api_route(
        path = '/patient/{id}',
        methods = ['POST'],
        endpoint = AICreator(
            DeepSeekModel,
            lambda note:
                f'''
                Read the following not from a doctor about a new visit and create a new "VisitTree".
                Note: {note}
                ''',
            VisitTree,
            VisitHandler,
            engine
        )
    )
    return router
