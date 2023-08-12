from odoo import models, fields

class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = "This is the model for our staff"
    _rec_name='name'
    _order='age asc'

    name = fields.Char(string="Name", size=50)
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    country_id = fields.Many2one('res.country', string='Country')
    country_ids = fields.Many2many('res.country', string='Countrys')
    country_code=fields.Char(string="Country Code", related="country_id.code")
    

