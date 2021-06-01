# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request,Response
import json
from odoo.tools import date_utils 

class HospitalManagement(http.Controller):
    @http.route('/hospital/', auth='public')
    def index(self, **kw):
        # return "Hello, world"
        return "Hello world"

    @http.route('/hospital/appointments/', csrf=False, auth='public', methods=['GET'])
    def list(self, **kw):
        ass = http.request.env['hospital.appointment'].sudo().search([])
        # res = {}
        # print(type(res))
        # for aa in ass:
        #     for a in aa._fields:
        #         print(a,aa[a])
        return Response(json.dumps(ass.read(),default=date_utils.json_default ),content_type='application/json',status=200) 
        # return http.request.render('hospital_management.listing', {
        #     'root': '/hospital/appointments',
        #     'objects': http.request.env['hospital.appointment'].sudo().search([]),
        # })

    @http.route('/hospital/appointments/<int:obj>/', auth='public', methods=['GET'],csrf=False)
    def object(self, obj, **kw):
        # return http.request.render('hospital_management.object', {
        #     'object': obj
        # })
        record = request.env['hospital.appointment'].sudo().search([('id','=',obj)])
        # print(type(record.read()))
        return Response(json.dumps(record.read(),default=date_utils.json_default ),content_type='application/json',status=200) 

    @http.route('/hospital/appointments/', type='json', auth='public', methods=['POST'],csrf=False)
    def create_appointments(self, **kw):
        if 0:#request.env['hospital.appointment'].sudo().search([('pat_id','=',kw['pat_id']),('doc_id','=',kw['doc_id']),('staatus','=','pending')]):
            return Response(json.dumps({'create':False}),content_type='application/json',status=200) 

        else:
            print(request.jsonrequest)
            record = http.request.env['hospital.appointment'].sudo().create(request.jsonrequest)
            rec  = request.env['hospital.appointment'].sudo().search([('id','=',record.id)])
            print(type(rec.read()),rec.read())
        return Response(json.dumps(record.read(),default=date_utils.json_default ),content_type='application/json',status=200) 

            

    @http.route('/hospital/appointments/<int:obj>/', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_appointments(self, obj, **kw):
        r = request.env['hospital.appointment'].sudo().search([('id','=',obj)])
        if r:
            record = r.sudo().write(request.jsonrequest)
            record = request.env['hospital.appointment'].sudo().search([('id','=',obj)])
            print(request.jsonrequest,record.read())
            return Response(json.dumps(record.read(),default=date_utils.json_default ),content_type='application/json',status=200) 
        else:
            return Response(json.dumps("No record Found"),content_type='application/json',status=200)
    @http.route('/hospital/appointments/<int:obj>/',  auth='public', methods=['DELETE'], csrf=False)
    def delete_appointments(self, obj, **kw):
        if request.env['hospital.appointment'].sudo().search([('id','=',obj)]):
            record = request.env['hospital.appointment'].sudo().search([('id','=',obj)])
            record.unlink()
            return Response(json.dumps(True),content_type='application/json',status=200)
        else:
            return Response(json.dumps(False),content_type='application/json',status=200)
