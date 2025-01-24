import datetime

from sqlmodel import Field, SQLModel


class ReviewData(SQLModel):
    '''Data model for a review.'''
    system: str = Field(description = "The system that was reviewed")
    note: str = Field(description = "The note for the review")

class ExamData(SQLModel):
    '''Data model for an exam.'''
    system: str = Field(description = "The system that was examined")
    note: str = Field(description = "The note for the exam")

class AssessmentData(SQLModel):
    '''Data model for an assessment.'''
    note: str = Field(description = "The note for the assessment")

class PlanData(SQLModel):
    '''Data model for a plan.'''
    note: str = Field(description = "The note for the plan")

class BillingData(SQLModel):
    '''Data model for billing information.'''
    code: str = Field(
        description = "The code for the billing item",
        regex = r'^\d{5}$'
    )
    note: str = Field(description = "The note for the billing item")

class DiagnosisData(SQLModel):
    '''Data model for a diagnosis.'''
    code: str = Field(
        description = "The code for the diagnosis",
        regex = r'^[A-Za-z]\d{2}\.[A-Za-z\d]{4}$'
    )
    note: str = Field(description = "The note for the diagnosis")

class VisitData(SQLModel):
    '''Data model for a visit.'''
    date: datetime.date
    type: str = Field(description = "The type of encounter")
    note: str = Field(description = "The note for the visit")

class PatientData(SQLModel):
    '''Data model for a patient.'''
    first_name: str = Field(description = "The first name of the patient")
    last_name: str = Field(description = "The last name of the patient")
    dob: datetime.date = Field(description = "The date of birth of the patient")
