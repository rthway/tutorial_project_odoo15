from odoo import models, fields, api, exceptions, _

# Define the RestStaff model
class RestStaff(models.Model):
    _name = 'rest.staff'
    _description = "This is the model for our staff"
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'age asc'
    
    # Fields of the RestStaff model
    name = fields.Char(string="Name", track_visibility="always", required=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", default="male")
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    dob = fields.Date(string="DOB")
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")
    country_id = fields.Many2one('res.country', string='Country')
    country_ids = fields.Many2many('res.country', string='Countries')
    country_code = fields.Char(string="Country Code", related="country_id.code")
    staff_line_ids = fields.One2many('rest.staff.lines', 'connecting_field', string='Staff Line')
    sequence = fields.Integer(string="Sequence")
    status = fields.Selection([('active','Active'),('resigned','Resigned')], string="Status", readonly=True, default="active")
    image = fields.Binary(string="Image", track_visibility="always")
    hand_salary = fields.Float(string="In Hand Salary")
    epf_esi = fields.Float(string="EPF+ESI")
    ctc_salary = fields.Float(string="CTC", compute="calc_ctc")
    seq_num = fields.Char(string="Seq. No.", readonly=True, copy=False, index=True, default=lambda self: self._generate_staff_id())

    # Custom method: Print a message when executed
    def new_fun(self):
        print("Executed a function by object button .............")
    
    # Custom method: Delete related records and show a notification
    def delete_one2many(self):
        for record in self:
            if record.staff_line_ids:
                record.staff_line_ids = [(5, 0, 0)]
                return {
                    'effect': {
                        'fadeout': 'slow',
                        'type': 'rainbow_man',
                        'message': 'Record has been deleted successfully'
                    }
                }
   
    # Custom method: Set the 'status' field to 'resigned'
    def do_resign(self):
        for rec in self:
            rec.status = 'resigned'
    
    # Validation constraint: Age must be between 18 and 100
    @api.constrains('age')
    def val_age(self):
        for record in self:
            if record.age <= 18 or record.age > 100:
                raise exceptions.ValidationError(_('Age must be between 18 and 100.'))

    # Custom method: Generate a unique staff ID using Odoo sequence
    @api.model
    def _generate_staff_id(self):
        seq = self.env['ir.sequence'].sudo().next_by_code('rest.seq.staff') or ''
        return seq

    # Compute the CTC salary based on 'hand_salary' and 'epf_esi'
    @api.depends('hand_salary', 'epf_esi')
    def calc_ctc(self):
        for record in self:
            ctc = 0
            if record.hand_salary:
                ctc += record.hand_salary
            if record.epf_esi:
                ctc += record.epf_esi
            record.ctc_salary = ctc

    # Compute the age based on the date of birth ('dob')
    @api.depends('dob')
    def _compute_age(self):
        today = fields.Date.today()
        for record in self:
            if record.dob:
                dob = fields.Date.from_string(record.dob)
                delta = today - dob
                record.age = delta.days // 365  # Approximate age in years
            else:
                record.age = 0
    
    # Override the default 'create' method to add custom logic
    @api.model
    def create(self, vals):
        existing_staff = self.search([('name', '=', vals.get('name'))])
        if existing_staff:
            raise exceptions.ValidationError(_("A staff with this name already exists."))
        return super(RestStaff, self).create(vals)

    # Supercalled unlink method with conditions
    # @api.ondelete
    def unlink(self):
        for record in self:
            if record.status == 'active':
                raise exceptions.ValidationError(_("You cannot delete a record in the 'Active' status."))
        return super(RestStaff, self).unlink()


    
# Define the RestStaffLines model
class RestStaffLines(models.Model):
    _name = 'rest.staff.lines'
    _description = "This is the model for staff lines"

    connecting_field = fields.Many2one('rest.staff', string="Staff ID")
    name = fields.Char(string="Name", required=True)
    product_id = fields.Many2one('product.product', string="Product", required=True)
    sequence = fields.Integer(string="Sequence")

# ORM Methods --------------------------------
# 1. search
# 2. search_count
# 3. browse
# 4. ref
# 5. create 
# 6. write
# 7. copy
# 8. unlink

# ORM search ID
# def check_orm(self):
#     search_var = self.env['rest.staff'].search([])
#     print(search_var)

# ORM search name data using ID
# def check_orm(self):
#     search_var = self.env['rest.staff'].search([])
#     for rec in search_var:
#         print(rec.name)

# ORM search using domain data (print active male records only)
# def check_orm(self):
#     search_var = self.env['rest.staff'].search(['|', ('status', '=', 'active'), ('gender', '=', 'male')])
#     for rec in search_var:
#         print(rec.name)     

# ORM search count 
# def check_orm(self):
#     search_var = self.env['rest.staff'].search_count(['|', ('status', '=', 'active'), ('gender', '=', 'male')])
#     print(search_var)

# ORM Browse
# def check_orm(self):
#     search_var = self.env['rest.staff'].search([])
#     for rec in search_var:
#         print(rec.name)

