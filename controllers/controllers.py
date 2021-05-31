# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class HospitalManagement(http.Controller):
    @http.route('/hospital/', auth='public')
    def index(self, **kw):
        # return "Hello, world"
        return "Hello world"

    @http.route('/hospital/appointments/', auth='public', methods=['GET'])
    def list(self, **kw):
        # ass = http.request.env['hospital.appointment'].search([])
        # res = {}
        # print(type(res))
        # for aa in ass:
        #     for a in aa._fields:
        #         res[a]=aa[a]
        # return json.dumps(res)
        return http.request.render('hospital_management.listing', {
            'root': '/hospital/appointments',
            'objects': http.request.env['hospital.appointment'].search([]),
        })

    @http.route('/hospital/appointments/id/<model("hospital.appointment"):obj>/', auth='public', methods=['GET'])
    def object(self, obj, **kw):
        return http.request.render('hospital_management.object', {
            'object': obj
        })
