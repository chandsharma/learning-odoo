# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class HospitalManagement(http.Controller):
    @http.route('/hospital/', auth='public')
    def index(self, **kw):
        # return "Hello, world"
        return "Hello world"

    @http.route('/hospital/appointments/', csrf='False', auth='public', methods=['GET'])
    def list(self, **kw):
        # ass = http.request.env['hospital.appointment'].search([])
        # # res = {}
        # # print(type(res))
        # for aa in ass:
        #     for a in aa._fields:
        #         print(a,aa[a])
        # return json.dumps(res)
        return http.request.render('hospital_management.listing', {
            'root': '/hospital/appointments',
            'objects': http.request.env['hospital.appointment'].sudo().search([]),
        })

    @http.route('/hospital/appointments/id/<model("hospital.appointment"):obj>/', auth='public', methods=['GET'])
    def object(self, obj, **kw):
        return http.request.render('hospital_management.object', {
            'object': obj
        })

    @http.route('/hospital/appointments/', csrf='False', type='json', auth='public', methods=['POST'])
    def create_appointments(self, obj, **kw):
        if self.env['hospital.appointment'].search([('pat_id','=',kw['pat_id']),('doc_id','=',kw['doc_id']),('staatus','=','pending')]):
            return "Already Exists"
        else:
            return http.request.env['hospital.appointment'].sudo().create(kw)

    @http.route('/hospital/appointments/<model("hospital.appointment"):obj>/', type='json', auth='public', methods=['PUT'], crpf='False')
    def update_appointments(self, obj, **kw):
        if self.env['hospital.appointment'].sudo().search([('id','=',obj)]):
            http.request.env['hospital.appointment'].sudo().write(kw)
            return "Record Updated Successfully"
        else:
            return "Record doesn't exists"
    @http.route('/hospital/appointments/<model("hospital.appointment"):obj>/', type='json', auth='public', methods=['DELETE'], crpf='False')
    def delete_appointments(self, obj, **kw):
        if self.env['hospital.appointment'].sudo().search([('id','=',obj)]):
            record = self.env['hospital.appointment'].sudo().search([('id','=',obj)])
            record.unlink()
            return "Record Updated Successfully"
        else:
            return "Not exists"
