from odoo import http
from odoo.http import request


class MainController(http.Controller):
    @http.route('/ica/login', type='json', auth='none')
    def api_login(self, **kw):
        data = {'login': kw.get('login'), 'password': kw.get('password'), 'type': 'password'}
        uid = request.session.authenticate(request.session.db, data)
        return {"message": "login success.", "uid": uid}

    @http.route(['/ica_elearning/list'], type='json', auth='user')
    def ica_elearning_list(self, **kw):
        data = request.env['res.partner'].search_read([], fields=['name'])
        return {"message": "Hello", "data": data}

    @http.route('/ica_elearning/details/<model("res.partner"):partner_id>', type='json', auth='user')
    def ica_elearning_details(self,partner_id,**kw):
        # partner_id = request.env['res.partner'].browse(partner_id).read(fields=['name'])
        return {"message": "Hello", "data": partner_id.read(fields=['name'])}
