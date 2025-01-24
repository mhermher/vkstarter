import os
from typing import Callable, Type

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from sqlmodel import Session, SQLModel

from vkstarter.model.handler import Handler

API_KEY = SecretStr(os.environ.get("OPENAI_API_KEY") or '')

class AICreator[T: SQLModel, R: SQLModel]:
    '''AI Model to create records.'''
    def __init__(
        self,
        prompt: Callable[[str], str],
        validator: Type[T],
        handler: Handler[T, R]
    ) -> None:
        '''Initialize the AI.'''
        self.__model = ChatOpenAI(model="gpt-4o-mini", api_key = API_KEY).with_structured_output(validator)
        self.__template = ChatPromptTemplate([
            (
                'system',
                '''
                You are a AI tool which assists doctors in creating patient records.
                You will be given a note on how to create new patient information.

                {instruction}
                '''
            )
        ])
        self.__prompt = prompt
        self.__validator = validator
        self.__handler = handler
    def invoke(self, note: str) -> T:
        '''Invoke the model.'''
        prompt = self.__template.invoke({'instruction': self.__prompt(note)})
        output = self.__validator.model_validate(self.__model.invoke(prompt))
        return output
    def __call__(self, note: str, session: Session) -> R:
        '''Handle a request.'''
        output = self.invoke(note)
        record = self.__handler.post(output, session)
        return record



class AIUpdater[T: SQLModel, R: SQLModel]:
    '''AI which returns structured information.'''
    def __init__(
        self,
        prompt: Callable[[T, str], str],
        validator: Type[T],
        handler: Handler[T, R]
    ) -> None:
        '''Initialize AI.'''
        self.__model = ChatOpenAI(model="gpt-4o-mini", api_key = API_KEY).with_structured_output(validator)
        self.__template = ChatPromptTemplate([
            (
                'system',
                '''
                You are a AI tool which assists doctors in updating patient records.
                You will be given patient information and a note on how to create new patient
                information.

                {instruction}
                '''
            )
        ])
        self.__prompt = prompt
        self.__validator = validator
        self.__handler = handler
    def invoke(self, input: T, note: str) -> T:
        '''Invoke the model.'''
        prompt = self.__template.invoke({'instruction': self.__prompt(input, note)})
        output = self.__validator.model_validate(self.__model.invoke(prompt))
        return output
    def __call__(self, id: int, note: str, session: Session) -> R:
        '''Handle a request.'''
        input = self.__validator.model_validate(self.__handler.get(id, session))
        output = self.invoke(input, note)
        record = self.__handler.put(id, output, session)
        return record
