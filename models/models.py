# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime

class hospital_patients (models.Model):
    _name = 'hospital.patients'

    #@api.onchange('dob')
    def _age(self):
        if self.dob:
            dob = datetime.strptime(str(self.dob), "%Y-%m-%d")
            age_calc = (datetime.today() - dob).days/365
            print('\n\n\n')
            print(str(self.dob))
            print(int(age_calc))
            self.age = int(age_calc)

    name = fields.Char(
        string='name',
    )
    dob = fields.Date(string='DOB')
    image = fields.Binary("Image")
    diseases = fields.Char(string='Diseases')
    age = fields.Integer(string='Age (years)',compute="_age")
    # name = fields.Char(default=lambda self: self._default_name())


class hospital_staff (models.Model):
    _name = 'hospital.staff'

    @api.onchange('dob')
    def _age(self):
        if self.dob:
            dob = datetime.strptime(str(self.dob), "%Y-%m-%d")
            age_calc = (datetime.today() - dob).days/365
            print('\n\n\n')
            print(str(self.dob))
            print(int(age_calc))
            self.age = int(age_calc)
    name = fields.Char(
        string='name',
    )
    dob = fields.Date(string='DOB')
    age = fields.Integer(string='Age (years)',compute="_age")

    
    