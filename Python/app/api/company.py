from fastapi import APIRouter
from app.models.company import CompanyResponse, CompanyEdit
from app.services.company_service import CompanyService

router = APIRouter(prefix = "/company", tags=["company"])

company_service = CompanyService()

@router.get("/", response_model = CompanyResponse)
def show_company_info():
    return company_service.show_company_info()

@router.put("/", response_model = CompanyResponse)
def change_company_info(company: CompanyEdit):
    return company_service.change_company_info(company)