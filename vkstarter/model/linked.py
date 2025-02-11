from sqlmodel import Field, SQLModel

from .data import AssessmentData, BillingData, DiagnosisData, ExamData, PatientData, PlanData, ReviewData, VisitData


class ReviewLink(ReviewData):
    '''Link model for a review.'''
    visit_id: int = Field(foreign_key = 'visitrecord.id')

class ExamLink(ExamData):
    '''Link model for an exam.'''
    visit_id: int = Field(foreign_key = 'visitrecord.id')

class AssessmentLink(AssessmentData):
    '''Link model for an assessment.'''
    visit_id: int = Field(foreign_key = 'visitrecord.id')
    diagnosis_id: int = Field(foreign_key = 'diagnosisrecord.id')

class PlanLink(PlanData):
    '''Link model for a plan.'''
    visit_id: int = Field(foreign_key = 'visitrecord.id')
    diagnosis_id: int = Field(foreign_key = 'diagnosisrecord.id')

class BillingLink(BillingData):
    '''Link model for billing information.'''
    visit_id: int = Field(foreign_key = 'visitrecord.id')
    diagnosis_id: int = Field(foreign_key = 'diagnosisrecord.id')

class DiagnosisLink(DiagnosisData):
    '''Link model for a diagnosis.'''
    patient_id: int = Field(foreign_key = 'patientrecord.id')

class VisitLink(VisitData):
    '''Link model for a visit.'''
    patient_id: int = Field(foreign_key = 'patientrecord.id')

class PatientLink(PatientData):
    '''Link model for a patient.'''
    pass
