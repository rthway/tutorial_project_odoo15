from odoo import models, fields,api,exceptions, _

class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = "This is the model for our staff"
    _rec_name='name'
    _order='age asc'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    country_id = fields.Many2one('res.country', string='Country')
    country_ids = fields.Many2many('res.country', string='Countrys')
    country_code=fields.Char(string="Country Code", related="country_id.code")
    staff_line_ids = fields.One2many('rest.staff.lines', 'connecting_field', string='Staff Line')
    
    @api.model
    def create(self, vals):
        existing_staff = self.search([('name', '=', vals.get('name'))])
        if existing_staff:
            raise exceptions.ValidationError(_("A staff with this name already exists."))
        return super(RestStaff, self).create(vals)
    
class RestStaffLines(models.Model):
    _name = 'rest.staff.lines'
    _description = "This is the model for staff lines"

    connecting_field = fields.Many2one('rest.staff', string="Staff ID")
    name = fields.Char(string="Name",  required=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)