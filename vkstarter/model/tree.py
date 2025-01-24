from typing import List, Sequence, Union

from .data import AssessmentData, BillingData, DiagnosisData, ExamData, PatientData, PlanData, ReviewData, VisitData


class ReviewTree(ReviewData):
    '''Tree model for a review.'''
    visit_id: int

class ExamTree(ExamData):
    '''Tree model for an exam.'''
    visit_id: int

class AssessmentTree(AssessmentData):
    '''Tree model for an assessment.'''
    visit_id: int
    diagnosis_id: int

class PlanTree(PlanData):
    '''Tree model for a plan.'''
    visit_id: int
    diagnosis_id: int

class BillingTree(BillingData):
    '''Tree model for billing information.'''
    visit_id: int
    diagnosis_id: int

class DiagnosisTree(DiagnosisData):
    '''Tree model for a diagnosis.'''
    patient_id: int
    assessments: List['AssessmentTree']
    plans: List['PlanTree']
    billings: List['BillingTree']

class VisitTree(VisitData):
    '''Tree model for a visit.'''
    patient_id: int
    reviews: List['ReviewTree']
    exams: List['ExamTree']
    assessments: List['AssessmentTree']
    plans: List['PlanTree']
    billings: List['BillingTree']

class PatientLeftTree(PatientData):
    '''Tree model for a patient.'''
    visits: Sequence['VisitData']
    diagnoses: Sequence['DiagnosisTree']

class PatientRightTree(PatientData):
    '''Tree model for a patient.'''
    visits: Sequence['VisitTree']
    diagnoses: Sequence['DiagnosisData']

PatientTree = Union[PatientLeftTree, PatientRightTree]
