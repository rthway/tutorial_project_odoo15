from odoo import models, fields,api,exceptions, _

class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = "This is the model for our staff"
    _rec_name='name'
    _inherit=['mail.thread','mail.activity.mixin']
    _order='age asc'

    def new_fun(self):
        print("Exucuted a function by object button .............")
    
    def delete_one2many(self):
        for record in self:
            if record.staff_line_ids:
                record.staff_line_ids=[(5,0,0)]
                return{
                    'effect':{
                        'fadeout':'slow',
                        'type':'rainbow_man',
                        'message':'Record has benn deleted succesufully'
                    }
                }


    def do_resign(self):
        for rec in self:
            rec.status= 'resigned'
    
    @api.constrains('age')
    def val_age(self):
        for record in self:
            if record.age<=18:
                raise exceptions.ValidationError(_('The age must be above then 18'))



    name = fields.Char(string="Name", track_visibility="always")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender", default="male")
    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    country_id = fields.Many2one('res.country', string='Country')
    country_ids = fields.Many2many('res.country', string='Countrys')
    country_code=fields.Char(string="Country Code", related="country_id.code")
    staff_line_ids = fields.One2many('rest.staff.lines', 'connecting_field', string='Staff Line')
    sequence = fields.Integer(string="seq.")
    status = fields.Selection([('active','Active'),('resigned','Resigned')],string="Status", readonly=True, default="active")
    image = fields.Binary(string="Image")
    hand_salary = fields.Float(string="In Hand Salary")
    epf_esi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC", compute="calc_ctc")

    @api.depends('hand_salary','epf_esi')
    def calc_ctc(self):
        for record in self:
            ctc = 0
            if record.hand_salary:
                ctc = ctc+record.hand_salary
            if record.epf_esi:
                ctc = ctc+record.epf_esi
            record.ctc_salary = ctc


    
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
    sequence = fields.Integer(string="seq.")
