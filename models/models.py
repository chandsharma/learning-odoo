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
    staff_id = fields.Many2one('hospital.staff',  ondelete='restrict',String="Staff Assigned")


class hospital_staff (models.Model):
    _name = 'hospital.staff'

    # @api.onchange('dob')
    def _age(self):
        for i in self:
            if i.dob:
                dob = datetime.strptime(str(i.dob), "%Y-%m-%d")
                age_calc = (datetime.today() - dob).days/365
                print('\n\n\n')
                print(str(i.dob))
                print(int(age_calc))
                i.age = int(age_calc)
    name = fields.Char(
        string='name',)
    dob = fields.Date(string='DOB')
    age = fields.Integer(string='Age (years)',compute="_age")
    entry_time = fields.Datetime(
        string='Entry',)
    exit_time = fields.Datetime(
        string='Exit', )
    salary = fields.Integer(string='Salary')
    patient_assigned = fields.One2many('hospital.patients','staff_id', String="Patients Assigned")

    
class hospital_doctor (models.Model):
    _name = 'hospital.doctor'

    # @api.onchange('dob')
    def _age(self):
        for i in self:
            if i.dob:
                dob = datetime.strptime(str(i.dob), "%Y-%m-%d")
                age_calc = (datetime.today() - dob).days/365
                i.age = int(age_calc)
    name = fields.Char(
        string='name',)
    dob = fields.Date(string='DOB')
    age = fields.Integer(string='Age (years)',compute="_age")
    speciality = fields.Selection(string='speciality', selection=[('cardio', 'Cardio'),('ortho','Ortho'),('neuro','Neuro'),('uro','Uro'),('gyno','Gyno'),('dento','Dento')])