from typing import List

from .atom import AssessmentAtom, BillingAtom, DiagnosisAtom, ExamAtom, PatientAtom, PlanAtom, ReviewAtom, VisitAtom


class ReviewHead(ReviewAtom):
    '''Head model for a review.'''
    pass

class ExamHead(ExamAtom):
    '''Head model for an exam.'''
    pass

class AssessmentHead(AssessmentAtom):
    '''Head model for an assessment.'''
    pass

class PlanHead(PlanAtom):
    '''Head model for a plan.'''
    pass

class BillingHead(BillingAtom):
    '''Head model for billing information.'''
    pass

class DiagnosisHead(DiagnosisAtom):
    '''Head model for a diagnosis.'''
    assessments: List['AssessmentHead']
    plans: List['PlanHead']
    billings: List['BillingHead']

class VisitHead(VisitAtom):
    '''Head model for a visit.'''
    reviews: List['ReviewHead']
    exams: List['ExamHead']
    assessments: List['AssessmentHead']
    plans: List['PlanHead']
    billings: List['BillingHead']

class PatientLeftHead(PatientAtom):
    '''Head model for a patient.'''
    visits: List['VisitAtom']
    diagnoses: List['DiagnosisHead']

class PatientRightHead(PatientAtom):
    '''Head model for a patient.'''
    visits: List['VisitHead']
    diagnoses: List['DiagnosisAtom']
