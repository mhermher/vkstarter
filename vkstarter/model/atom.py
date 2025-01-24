from sqlmodel import Field

from .linked import AssessmentLink, BillingLink, DiagnosisLink, ExamLink, PatientLink, PlanLink, ReviewLink, VisitLink


class ReviewAtom(ReviewLink):
    '''Atom model for a review.'''
    id: int = Field(default=None, primary_key=True)

class ExamAtom(ExamLink):
    '''Atom model for an exam.'''
    id: int = Field(default=None, primary_key=True)

class AssessmentAtom(AssessmentLink):
    '''Atom model for an assessment.'''
    id: int = Field(default=None, primary_key=True)

class PlanAtom(PlanLink):
    '''Atom model for a plan.'''
    id: int = Field(default=None, primary_key=True)

class BillingAtom(BillingLink):
    '''Atom model for billing information.'''
    id: int = Field(default=None, primary_key=True)

class DiagnosisAtom(DiagnosisLink):
    '''Atom model for a diagnosis.'''
    id: int = Field(default=None, primary_key=True)

class VisitAtom(VisitLink):
    '''Atom model for a visit.'''
    id: int = Field(default=None, primary_key=True)

class PatientAtom(PatientLink):
    '''Atom model for a patient.'''
    id: int = Field(default=None, primary_key=True)
