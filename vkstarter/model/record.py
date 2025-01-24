from typing import List, Optional

from sqlmodel import Field, Relationship

from .linked import AssessmentLink, BillingLink, DiagnosisLink, ExamLink, PatientLink, PlanLink, ReviewLink, VisitLink


class ReviewRecord(ReviewLink, table=True):
    '''Record model for a review.'''
    id: Optional[int] = Field(primary_key = True, default = None)
    visit: 'VisitRecord' = Relationship(back_populates='reviews')

class ExamRecord(ExamLink, table=True):
    '''Record model for an exam.'''
    id: Optional[int] = Field(primary_key = True, default = None)
    visit: 'VisitRecord' = Relationship(back_populates='exams')

class AssessmentRecord(AssessmentLink, table=True):
    '''Record model for an assessment.'''
    id: Optional[int] = Field(primary_key = True, default = None)
    visit: 'VisitRecord' = Relationship(back_populates='assessments')
    diagnosis: 'DiagnosisRecord' = Relationship(back_populates='assessments')

class PlanRecord(PlanLink, table=True):
    '''Record model for a plan.'''
    id: Optional[int] = Field(primary_key = True, default = None)
    visit: 'VisitRecord' = Relationship(back_populates='plans')
    diagnosis: 'DiagnosisRecord' = Relationship(back_populates='plans')

class BillingRecord(BillingLink, table=True):
    '''Record model for billing information.'''
    id: Optional[int] = Field(primary_key = True, default = None)
    visit: 'VisitRecord' = Relationship(back_populates='billings')
    diagnosis: 'DiagnosisRecord' = Relationship(back_populates='billings')

class DiagnosisRecord(DiagnosisLink, table=True):
    '''Record model for a diagnosis.'''
    id: Optional[int] = Field(primary_key = True, default = None)
    patient: 'PatientRecord' = Relationship(back_populates='diagnoses')
    assessments: List['AssessmentRecord'] = Relationship(back_populates='diagnosis')
    plans: List['PlanRecord'] = Relationship(back_populates='diagnosis')
    billings: List['BillingRecord'] = Relationship(back_populates='diagnosis')

class VisitRecord(VisitLink, table=True):
    '''Record model for a visit.'''
    id: Optional[int] = Field(primary_key = True, default = None)
    patient: 'PatientRecord' = Relationship(back_populates='visits')
    reviews: List['ReviewRecord'] = Relationship(back_populates='visit')
    exams: List['ExamRecord'] = Relationship(back_populates='visit')
    assessments: List['AssessmentRecord'] = Relationship(back_populates='visit')
    plans: List['PlanRecord'] = Relationship(back_populates='visit')
    billings: List['BillingRecord'] = Relationship(back_populates='visit')

class PatientRecord(PatientLink, table=True):
    '''Record model for a patient.'''
    id: Optional[int] = Field(primary_key = True, default = None)
    visits: List['VisitRecord'] = Relationship(back_populates='patient')
    diagnoses: List['DiagnosisRecord'] = Relationship(back_populates='patient')
