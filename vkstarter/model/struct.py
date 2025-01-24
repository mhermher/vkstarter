from .head import (
    AssessmentHead,
    BillingHead,
    DiagnosisHead,
    ExamHead,
    PatientLeftHead,
    PatientRightHead,
    PlanHead,
    ReviewHead,
    VisitHead,
)
from .tail import (
    AssessmentLeftTail,
    AssessmentRightTail,
    BillingLeftTail,
    BillingRightTail,
    DiagnosisTail,
    ExamTail,
    PatientTail,
    PlanLeftTail,
    PlanRightTail,
    ReviewTail,
    VisitTail,
)


class ReviewStruct(ReviewHead, ReviewTail):
    '''Struct model for a review.'''
    pass

class ExamStruct(ExamHead, ExamTail):
    '''Struct model for an exam.'''
    pass

class AssessmentLeftStruct(AssessmentHead, AssessmentLeftTail):
    '''Struct model for an assessment.'''
    pass

class AssessmentRightStruct(AssessmentHead, AssessmentRightTail):
    '''Struct model for an assessment.'''
    pass

class PlanLeftStruct(PlanHead, PlanLeftTail):
    '''Struct model for a plan.'''
    pass

class PlanRightStruct(PlanHead, PlanRightTail):
    '''Struct model for a plan.'''
    pass

class BillingLeftStruct(BillingHead, BillingLeftTail):
    '''Struct model for billing information.'''
    pass

class BillingRightStruct(BillingHead, BillingRightTail):
    '''Struct model for billing information.'''
    pass

class DiagnosisStruct(DiagnosisHead, DiagnosisTail):
    '''Struct model for a diagnosis.'''
    pass

class VisitStruct(VisitHead, VisitTail):
    '''Struct model for a visit.'''
    pass

class PatientLeftStruct(PatientLeftHead, PatientTail):
    '''Struct model for a patient.'''
    pass

class PatientRightStruct(PatientRightHead, PatientTail):
    '''Struct model for a patient.'''
    pass
