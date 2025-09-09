from app.models.company import Company, CompanyResponse, CompanyEdit

class CompanyService:
    def __init__(self):
        self._name = "Empresa teste"
        self._address = "Rua K, Setor Bueno, nº 456"
        self._phone = "9 9999-1111"
        self._main_email = "teste@gmail.com"
        self._company = Company(name=self._name, address=self._address, phone=self._phone, main_email=self._main_email)
    
    def show_company_info(self) -> CompanyResponse:
        return CompanyResponse(name = self._company.name, address=self._company.address, phone = self._company.phone, main_email = self._company.main_email)
    
    def change_company_info(self, edit_data: CompanyEdit) -> CompanyResponse:
        if edit_data.name is not None:
            self._company.name = edit_data.name
        if edit_data.address is not None:
            self._company.address = edit_data.address
        if edit_data.phone is not None:
            self._company.phone = edit_data.phone
        if edit_data.main_email is not None:
            self._company.main_email = edit_data.main_email

        return self.show_company_info()

    
    