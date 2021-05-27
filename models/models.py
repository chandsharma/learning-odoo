# -*- coding: utf-8 -*-


from odoo import models, fields, api
from datetime import date, datetime
from odoo.exceptions import UserError,ValidationError

class hospital_patients (models.Model):
    _name = 'hospital.patients'

    # @api.onchange('dob')
    def _age(self):
        for i in self:
            if i.dob:
                dob = datetime.strptime(str(i.dob), "%Y-%m-%d")
                age_calc = (datetime.today() - dob).days/365
                i.age = int(age_calc)

    name = fields.Char(
        string='name',
    )
    dob = fields.Date(string='DOB')
    image = fields.Binary("Image")
    diseases = fields.Char(string='Diseases')
    age = fields.Integer(string='Age (years)',compute="_age")
    # name = fields.Char(default=lambda self: self._default_name())
    staff_id = fields.Many2one('hospital.staff',  ondelete='restrict',String="Staff Assigned")

    def name_get(self):
        l = []
        for p in self:
            name = p.name
            name += " ({})".format(p.age)
            l.append((p.id,name))
        print(l)
        return l


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
    entry_time = fields.Float(string='Entry', )#compute="_compute_time")
    exit_time = fields.Float(string='Exit', )#compute="_compute_time")
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
    
    def name_get(self):
        l = []
        for d in self:
            name = d.name
            name += " ({})".format(d.speciality)
            l.append((d.id,name))
        print(l)
        return l

class hospital_appointment (models.Model):
    _name = 'hospital.appointment'

    pat_id = fields.Many2one('hospital.patients',  ondelete='restrict',String="Patient")
    doc_id = fields.Many2one('hospital.doctor',  ondelete='restrict',String="Doctor")
    pic = fields.Binary(related='pat_id.image')
    time = fields.Float(string='Time',)# compute="_compute_time")
    staatus = fields.Selection(string='Status', selection=[('pending', 'Pending'),('done','Done')], default='pending')
    discription = fields.Char(string="Discription")
    amount = fields.Float(string='Amount')

    @api.model
    def create(self, values):
        # print(type(values),values)
        # print(type(values),values)
        exists = self.env['hospital.appointment'].search([('pat_id','=',values['pat_id']),('doc_id','=',values['doc_id']),('staatus','=','pending')])
        #check status pending
        if exists:
            raise UserError('Appointment already exists!')
        rt = super(hospital_appointment,self).create(values)
        return rt

    def testbutton(self):
        pass

    

# soft delete appointments
# check and over-write create()

class hospital_genadd(models.Model):
    _inherit = 'hospital.patients'

    address = fields.Char(string="Address")
    
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('nonbianry', 'Non-Binary')])
    
class hospital_gena(models.Model):
    _inherit = 'hospital.staff'

    address = fields.Char(string="Address")
    
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('nonbianry', 'Non-Binary')])
    
class hospital_genad(models.Model):
    _inherit = 'hospital.doctor'

    address = fields.Char(string="Address")
    
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'), ('nonbianry', 'Non-Binary')])