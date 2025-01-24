from .atom import AssessmentAtom, BillingAtom, DiagnosisAtom, ExamAtom, PatientAtom, PlanAtom, ReviewAtom, VisitAtom


class ReviewTail(ReviewAtom):
    '''Tail model for a review.'''
    visit: 'VisitTail'

class ExamTail(ExamAtom):
    '''Tail model for an exam.'''
    visit: 'VisitTail'

class AssessmentLeftTail(AssessmentAtom):
    '''Tail model for an assessment.'''
    visit: 'VisitAtom'
    diagnosis: 'DiagnosisTail'

class AssessmentRightTail(AssessmentAtom):
    '''Tail model for an assessment.'''
    visit: 'VisitTail'
    diagnosis: 'DiagnosisAtom'

class PlanLeftTail(PlanAtom):
    '''Tail model for a plan.'''
    visit: 'VisitAtom'
    diagnosis: 'DiagnosisTail'

class PlanRightTail(PlanAtom):
    '''Tail model for a plan.'''
    visit: 'VisitTail'
    diagnosis: 'DiagnosisAtom'

class BillingLeftTail(BillingAtom):
    '''Tail model for billing information.'''
    visit: 'VisitAtom'
    diagnosis: 'DiagnosisTail'

class BillingRightTail(BillingAtom):
    '''Tail model for billing information.'''
    visit: 'VisitTail'
    diagnosis: 'DiagnosisAtom'

class DiagnosisTail(DiagnosisAtom):
    '''Tail model for a diagnosis.'''
    patient: 'PatientTail'

class VisitTail(VisitAtom):
    '''Tail model for a visit.'''
    patient: 'PatientTail'

class PatientTail(PatientAtom):
    '''Tail model for a patient.'''
    pass
