from typing import Protocol, override

from fastapi import HTTPException
from sqlmodel import Session, SQLModel

from vkstarter.model.record import (
    AssessmentRecord,
    BillingRecord,
    DiagnosisRecord,
    ExamRecord,
    PatientRecord,
    PlanRecord,
    ReviewRecord,
    VisitRecord,
)
from vkstarter.model.tree import (
    AssessmentTree,
    BillingTree,
    DiagnosisTree,
    ExamTree,
    PatientLeftTree,
    PatientTree,
    PlanTree,
    ReviewTree,
    VisitTree,
)


class Handler[T: SQLModel, R: SQLModel](Protocol):
    '''Handler for record type.'''
    @staticmethod
    def get(id: int, session: Session) -> R:
        '''Get the record by ID.'''
        ...
    @staticmethod
    def post(link: T, session: Session) -> R:
        '''Create a new record from tree.'''
        ...
    @staticmethod
    def put(id: int, tree: T, session: Session) -> R:
        '''Update an existing record with tree.'''
        ...
    @staticmethod
    def delete(id: int, session: Session) -> None:
        '''Delete an existing record by ID.'''
        ...


class PlanHandler(Handler[PlanTree, PlanRecord]):
    '''Handler for plan records.'''
    tree = PlanTree
    record = PlanRecord
    @staticmethod
    @override
    def get(id: int, session: Session) -> PlanRecord:
        '''Get a plan record by ID.'''
        record = session.get(PlanRecord, id)
        if record is None:
            raise HTTPException(status_code = 404, detail = "Plan not found")
        return record
    @staticmethod
    @override
    def post(link: PlanTree, session: Session) -> PlanRecord:
        '''Create a new plan record.'''
        diagnosis = session.get(DiagnosisRecord, link.diagnosis_id)
        if diagnosis is None:
            raise HTTPException(status_code = 404, detail = "Diagnosis not found")
        visit = session.get(VisitRecord, link.visit_id)
        if visit is None:
            raise HTTPException(status_code = 404, detail = "Visit not found")
        if visit.patient_id != diagnosis.patient_id:
            raise HTTPException(status_code = 400, detail = "Diagnosis and visit do not match")
        record = PlanRecord.model_validate(link)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    @staticmethod
    @override
    def put(id: int, tree: PlanTree, session: Session) -> PlanRecord:
        '''Update an existing plan record.'''
        record = PlanHandler.get(id, session)
        update = record.sqlmodel_update(tree.model_dump())
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    @staticmethod
    @override
    def delete(id: int, session: Session) -> None:
        '''Delete a plan record by ID.'''
        record = PlanHandler.get(id, session)
        session.delete(record)
        session.commit()

class BillingHandler(Handler[BillingTree, BillingRecord]):
    '''Handler for billing records.'''
    tree = BillingTree
    record = BillingRecord
    @staticmethod
    @override
    def get(id: int, session: Session) -> BillingRecord:
        '''Get a billing record by ID.'''
        record = session.get(BillingRecord, id)
        if record is None:
            raise HTTPException(status_code = 404, detail = "Billing not found")
        return record
    @staticmethod
    @override
    def post(link: BillingTree, session: Session) -> BillingRecord:
        '''Create a new billing record.'''
        diagnosis = session.get(DiagnosisRecord, link.diagnosis_id)
        if diagnosis is None:
            raise HTTPException(status_code = 404, detail = "Diagnosis not found")
        visit = session.get(VisitRecord, link.visit_id)
        if visit is None:
            raise HTTPException(status_code = 404, detail = "Visit not found")
        if visit.patient_id != diagnosis.patient_id:
            raise HTTPException(status_code = 400, detail = "Diagnosis and visit do not match")
        record = BillingRecord.model_validate(link)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    @staticmethod
    @override
    def put(id: int, tree: BillingTree, session: Session) -> BillingRecord:
        '''Update an existing billing record.'''
        record = BillingHandler.get(id, session)
        update = record.sqlmodel_update(tree.model_dump())
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    @staticmethod
    @override
    def delete(id: int, session: Session) -> None:
        '''Delete a billing record by ID.'''
        record = BillingHandler.get(id, session)
        session.delete(record)
        session.commit()

class AssessmentHandler(Handler[AssessmentTree, AssessmentRecord]):
    '''Handler for assessment records.'''
    tree = AssessmentTree
    record = AssessmentRecord
    @staticmethod
    @override
    def get(id: int, session: Session) -> AssessmentRecord:
        '''Get an assessment record by ID.'''
        record = session.get(AssessmentRecord, id)
        if record is None:
            raise HTTPException(status_code = 404, detail = "Assessment not found")
        return record
    @staticmethod
    @override
    def post(link: AssessmentTree, session: Session) -> AssessmentRecord:
        '''Create a new assessment record.'''
        diagnosis = session.get(DiagnosisRecord, link.diagnosis_id)
        if diagnosis is None:
            raise HTTPException(status_code = 404, detail = "Diagnosis not found")
        visit = session.get(VisitRecord, link.visit_id)
        if visit is None:
            raise HTTPException(status_code = 404, detail = "Visit not found")
        if visit.patient_id != diagnosis.patient_id:
            raise HTTPException(status_code = 400, detail = "Diagnosis and visit do not match")
        record = AssessmentRecord.model_validate(link)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    @staticmethod
    @override
    def put(id: int, tree: AssessmentTree, session: Session) -> AssessmentRecord:
        '''Update an existing assessment record.'''
        record = AssessmentHandler.get(id, session)
        update = record.sqlmodel_update(tree.model_dump())
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    @staticmethod
    @override
    def delete(id: int, session: Session) -> None:
        '''Delete an assessment record by ID.'''
        record = AssessmentHandler.get(id, session)
        session.delete(record)
        session.commit()

class ReviewHandler(Handler[ReviewTree, ReviewRecord]):
    '''Handler for review records.'''
    tree = ReviewTree
    record = ReviewRecord
    @staticmethod
    @override
    def get(id: int, session: Session) -> ReviewRecord:
        '''Get a review record by ID.'''
        record = session.get(ReviewRecord, id)
        if record is None:
            raise HTTPException(status_code = 404, detail = "Review not found")
        return record
    @staticmethod
    @override
    def post(link: ReviewTree, session: Session) -> ReviewRecord:
        '''Create a new review record.'''
        visit = session.get(VisitRecord, link.visit_id)
        if visit is None:
            raise HTTPException(status_code = 404, detail = "Visit not found")
        record = ReviewRecord.model_validate(link)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    @staticmethod
    @override
    def put(id: int, tree: ReviewTree, session: Session) -> ReviewRecord:
        '''Update an existing review record.'''
        record = ReviewHandler.get(id, session)
        update = record.sqlmodel_update(tree.model_dump())
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    @staticmethod
    @override
    def delete(id: int, session: Session) -> None:
        '''Delete a review record by ID.'''
        record = ReviewHandler.get(id, session)
        session.delete(record)
        session.commit()

class ExamHandler(Handler[ExamTree, ExamRecord]):
    '''Handler for exam records.'''
    tree = ExamTree
    record = ExamRecord
    @staticmethod
    @override
    def get(id: int, session: Session) -> ExamRecord:
        '''Get an exam record by ID.'''
        record = session.get(ExamRecord, id)
        if record is None:
            raise HTTPException(status_code = 404, detail = "Exam not found")
        return record
    @staticmethod
    @override
    def post(link: ExamTree, session: Session) -> ExamRecord:
        '''Create a new exam record.'''
        visit = session.get(VisitRecord, link.visit_id)
        if visit is None:
            raise HTTPException(status_code = 404, detail = "Visit not found")
        record = ExamRecord.model_validate(link)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    @staticmethod
    @override
    def put(id: int, tree: ExamTree, session: Session) -> ExamRecord:
        '''Update an existing exam record.'''
        record = ExamHandler.get(id, session)
        update = record.sqlmodel_update(tree.model_dump())
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    @staticmethod
    @override
    def delete(id: int, session: Session) -> None:
        '''Delete an exam record by ID.'''
        record = ExamHandler.get(id, session)
        session.delete(record)
        session.commit()

class DiagnosisHandler(Handler[DiagnosisTree, DiagnosisRecord]):
    '''Handler for diagnosis records.'''
    tree = DiagnosisTree
    record = DiagnosisRecord
    @staticmethod
    @override
    def get(id: int, session: Session) -> DiagnosisRecord:
        '''Get a diagnosis record by ID.'''
        record = session.get(DiagnosisRecord, id)
        if record is None:
            raise HTTPException(status_code = 404, detail = "Diagnosis not found")
        return record
    @staticmethod
    @override
    def post(link: DiagnosisTree, session: Session) -> DiagnosisRecord:
        '''Create a new diagnosis record.'''
        record = DiagnosisRecord.model_validate(link)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    @staticmethod
    @override
    def put(id: int, tree: DiagnosisTree, session: Session) -> DiagnosisRecord:
        '''Update an existing diagnosis record.'''
        record = DiagnosisHandler.get(id, session)
        update = record.sqlmodel_update(tree.model_dump())
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    @staticmethod
    @override
    def delete(id: int, session: Session) -> None:
        '''Delete a diagnosis record by ID.'''
        record = DiagnosisHandler.get(id, session)
        session.delete(record)
        session.commit()

class VisitHandler(Handler[VisitTree, VisitRecord]):
    '''Handler for visit records.'''
    tree = VisitTree
    record = VisitRecord
    @staticmethod
    @override
    def get(id: int, session: Session) -> VisitRecord:
        '''Get a visit record by ID.'''
        record = session.get(VisitRecord, id)
        if record is None:
            raise HTTPException(status_code = 404, detail = "Visit not found")
        return record
    @staticmethod
    @override
    def post(link: VisitTree, session: Session) -> VisitRecord:
        '''Create a new visit record.'''
        patient = session.get(PatientRecord, link.patient_id)
        if patient is None:
            raise HTTPException(status_code = 404, detail = "Patient not found")
        record = VisitRecord.model_validate(link)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    @staticmethod
    @override
    def put(id: int, tree: VisitTree, session: Session) -> VisitRecord:
        '''Update an existing visit record.'''
        record = VisitHandler.get(id, session)
        update = record.sqlmodel_update(tree.model_dump())
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    @staticmethod
    @override
    def delete(id: int, session: Session) -> None:
        '''Delete a visit record by ID.'''
        record = VisitHandler.get(id, session)
        session.delete(record)
        session.commit()

class PatientHandler(Handler[PatientLeftTree, PatientRecord]):
    '''Handler for patient records.'''
    tree = PatientLeftTree
    record = PatientRecord
    @staticmethod
    @override
    def get(id: int, session: Session) -> PatientRecord:
        '''Get a patient record by ID.'''
        record = session.get(PatientRecord, id)
        if record is None:
            raise HTTPException(status_code = 404, detail = "Patient not found")
        return record
    @staticmethod
    @override
    def post(link: PatientTree, session: Session) -> PatientRecord:
        '''Create a new patient record.'''
        record = PatientRecord.model_validate(link)
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    @staticmethod
    @override
    def put(id: int, tree: PatientTree, session: Session) -> PatientRecord:
        '''Update an existing patient record.'''
        record = PatientHandler.get(id, session)
        update = record.sqlmodel_update(tree.model_dump())
        session.add(update)
        session.commit()
        session.refresh(update)
        return update
    @staticmethod
    @override
    def delete(id: int, session: Session) -> None:
        '''Delete a patient record by ID.'''
        record = PatientHandler.get(id, session)
        session.delete(record)
        session.commit()
