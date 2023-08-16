# Tutorial_project_odoo15
## **Create a New Module:**

-   Odoo apps are organized as modules. Create a new directory for your module in the Odoo addons folder.
-   Create the necessary files, including the module manifest file (`__manifest__.py`).
Here's what a basic `__manifest__.py` file looks like:
```

    # -*- coding: utf-8 -*-
    {
        'name': 'Your Module Name',
        'version': '1.0',
        'summary': 'A short description of your module',
        'description': 'A more detailed description of your module',
        'author': 'Your Name',
        'website': 'Your Website',
        'category': 'Uncategorized',
        'depends': ['base'],  # List of module dependencies
        'data': [
            # List of XML files containing views, data, etc.
        ],
        'demo': [
            # List of demo data files
        ],
        'installable': True,
        'application': True,
        'auto_install': False,
    }
```

Let's go through the key fields in the `__manifest__.py` file:

-   `name`: The name of your module.
-   `version`: The version of your module. It's usually in the format 'X.Y' or 'X.Y.Z', where X is the major version, Y is the minor version, and Z is the patch version.
-   `summary`: A short, one-line description of your module.
-   `description`: A more detailed description of your module's functionality.
-   `author`: Your name or the name of your company.
-   `website`: Your website or the module's website.
-   `category`: The category under which your module should be listed (e.g., Sales, Inventory, Human Resources, etc.).
-   `depends`: A list of other module names that your module depends on. Odoo will ensure that these dependencies are met.
-   `data`: A list of paths to XML files that define views, data records, and other configurations for your module.
-   `demo`: A list of paths to XML files that contain demo data for your module.
-   `installable`: Indicates whether the module can be installed by users.
-   `application`: Indicates whether the module is an application module (as opposed to a library or utility).
-   `auto_install`: Whether the module should be automatically installed when its dependencies are installed.

Remember that the `__manifest__.py` file is just one part of developing an Odoo module. You'll need to create other files for models, views, workflows, security rules, and more, depending on the functionality of your module.

## Add an icon to your Odoo module 
To add an icon to your Odoo module, you can include an `icon` field in the `__manifest__.py` file. This icon will be displayed next to your module's name in the Odoo interface. Here's how you can add an icon to your module:

1.  **Choose an Icon:** Choose an icon that represents the theme or functionality of your module. Icons are usually in PNG format and are square with dimensions like 64x64 pixels.
    
2.  **Add the Icon to Your Module:** Place the icon file in your module's directory. You can name the icon file as `icon.png` or something similar.
    
3.  **Update `__manifest__.py`:** Edit your `__manifest__.py` file to include the `icon` field. You need to provide the relative path to your icon file.
    

Here's an example of how to add an icon to your module's `__manifest__.py`:

pythonCopy code

    # -*- coding: utf-8 -*-
    {
        'name': 'Your Module Name',
        'version': '1.0',
        'summary': 'A short description of your module',
        'description': 'A more detailed description of your module',
        'author': 'Your Name',
        'website': 'Your Website',
        'category': 'Uncategorized',
        'depends': ['base'],  # List of module dependencies
        'data': [
            # List of XML files containing views, data, etc.
        ],
        'demo': [
            # List of demo data files
        ],
        'installable': True,
        'application': True,
        'auto_install': False,
        'icon': 'static/description/icon.png',  # Relative path to your icon file
    }

In this example, the icon file (`icon.png`) is located in the `static/description/` directory relative to the module's root directory.

After making these changes, make sure to update the icon path to match the actual location of your icon file within your module's directory structure.

Remember that the icon file should be in PNG format and should be a square image. It's recommended to provide an icon with dimensions like 64x64 pixels for consistent display within the Odoo interface.

Once you've updated your `__manifest__.py` file, restart your Odoo instance or update your module to see the icon displayed next to your module's name in the Odoo interface.

1.  **Create the Module Directory:** Start by creating a directory named `rest_staff` in your Odoo addons folder.
    
2.  **Create `__manifest__.py`:** Create a `__manifest__.py` file in the `rest_staff` directory with the following content:
    

  

      
        # -*- coding: utf-8 -*-
        {
            'name': 'Resturant Management',
            'version': '1.0',
            'summary': 'Manage resturant records using a RESTful approach',
            'author': 'Roshan Kumar Thapaa',
            'category': 'others,
            'depends': ['base'],
            'data': [
                'views/staff_view.xml',
                'views/staff_menu.xml',
                'security/ir.model.access.csv',
            ],
            'demo': [],
            'installable': True,
            'application': True,
        }

3.  **Create Model and View:** Create a `models` folder within `rest_staff` and create a file named `staff.py` with the following content:



   

 

    
        
        from odoo import models, fields
        
        class Staff(models.Model):
            _name = 'rest.staff'
            _description = 'REST Staff'
    
        name = fields.Char(string='Name', required=True)
        age = fields.Integer(string='Age')
        gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other'),
        ], string='Gender')
        dob = fields.Date(string='Date of Birth')
        mobile = fields.Char(string='Mobile')
        email = fields.Char(string='Email')

4.  **Create Views:** Create a `views` folder within `rest_staff` and create a file named `staff_view.xml` with the following content:

```
    	<odoo>
                <data>
                    <record id="view_staff_form" model="ir.ui.view">
                        <field name="name">rest.staff.form</field>
                        <field name="model">rest.staff</field>
                        <field name="arch" type="xml">
                            <form>
                                <group>
                                    <field name="name"/>
                                    <field name="age"/>
                                    <field name="gender"/>
                                    <field name="dob"/>
                                    <field name="mobile"/>
                                    <field name="email"/>
                                </group>
                            </form>
                        </field>
                    </record>
                </data>
            </odoo>
            
```

5.  **Create Menu:** Create a file named `staff_menu.xml` within the `views` folder with the following content:

```

    <odoo>
        <data>
            <menuitem id="menu_staff" name="Staff" sequence="10"/>
            <menuitem id="menu_staff_list" name="Staff List" parent="menu_staff"
                      action="action_staff_list"/>
        </data>
    </odoo> 
```
6.  **Create Access Control:** Create a `security` folder within `rest_staff` and create a file named `ir.model.access.csv` with the following content:
   
```   id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
    access_staff_user,access_staff_user,model_rest_staff,,group_user,1,1,1,0
    access_staff_manager,access_staff_manager,model_rest_staff,,base.group_manager,1,1,1,1
```
7.  **Restart Odoo:** Restart your Odoo instance to load the new module.
    
8.  **Install the Module:** Install the module by going to "Apps" in Odoo and searching for "REST Staff Management." Install it, and the new menu item "Staff List" should be available under the "Staff" menu.
### Attributes of fields in odoo
In Odoo, fields are used to define the structure and behavior of database columns in models (also known as classes or tables). Each field in Odoo has certain attributes that define its behavior, presentation, and validation. Some common field attributes include:

1.  **string**: This attribute defines the label or display name of the field as shown to users.
    
2.  **help**: It provides additional information or hints about the purpose or expected value of the field.
    
3.  **required**: Determines whether the field must have a value before a record can be saved.
    
4.  **readonly**: Prevents users from modifying the field's value after a record is saved.
    
5.  **default**: Sets a default value for the field when a new record is created.
    
6.  **compute**: Specifies a method that calculates the value of the field dynamically based on other fields' values.
    
7.  **inverse**: Specifies a method that updates other fields when the value of this field changes.
    
8.  **store**: Indicates whether the field's value should be stored in the database. Computed fields, for instance, are usually not stored.
    
9.  **selection**: Defines a list of selectable options for the field, allowing users to choose from a predefined set of values.
    
10.  **related**: Establishes a link between the current field and a field in another model, allowing you to display data from related records.
    
11.  **domain**: Sets a domain expression that restricts the records that can be selected in a relational field.
    
12.  **copy**: Determines how the field's value is copied when duplicating records.
    
13.  **index**: Specifies whether an index should be created on the database column associated with the field, which can improve query performance.
    
14.  **size**: Defines the maximum length of text fields (e.g., Char fields).
    
15.  **digits**: Sets the precision (total digits) and scale (decimal places) for numerical fields (e.g., Float and Decimal fields).
16.  **invisible**: invisible attribute is commonly used in the XML views to control the visibility of fields based on certain conditions. When you set the invisible attribute to a field, you can use an expression to determine whether the field should be visible or not.

## @api on odoo
In Odoo, the `@api` decorators are used to define various types of methods that interact with records in the Odoo database. These methods can be used to perform various actions like creating, updating, deleting records, or executing business logic. Here are some common types of `@api` methods along with examples:

1.  **@api.model**: This decorator is used for methods that don't require any specific record from the model. They are typically utility methods that don't modify or retrieve specific records.



```
from odoo import models, api

class MyModel(models.Model):
    _name = 'my.model'

 @api.model
    def do_something(self):
        # Your logic here
        return result
```

2.  **@api.onchange**: This decorator is used for methods that are automatically triggered when the value of a specific field changes. These methods are useful for updating other fields or performing calculations based on the changed field.



```
from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.model'

    field_a = fields.Float(string='Field A')
    field_b = fields.Float(string='Field B')

 @api.onchange('field_a')
    def _onchange_field_a(self):
        self.field_b = self.field_a * 2
```     

3.  **@api.depends**: This decorator is used for computed fields or methods that depend on the values of specific fields. It ensures that the computed field is updated whenever the dependent fields change.


```
from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.model'

    field_a = fields.Float(string='Field A')
    field_b = fields.Float(string='Field B')
    computed_field = fields.Float(string='Computed Field', compute='_compute_field')

 @api.depends('field_a', 'field_b')
    def _compute_field(self):
        for record in self:
            record.computed_field = record.field_a + record.field_b
```
4.  **@api.constrains**: This decorator is used for methods that enforce constraints on records before they are saved to the database.



```
from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.model'

    field_c = fields.Float(string='Field C')

 @api.constrains('field_c')
    def _check_field_c(self):
        for record in self:
            if record.field_c < 0:
                raise models.ValidationError("Field C cannot be negative.")
``` 

5.  **@api.multi**: This decorator is used for methods that operate on multiple records. It's typically used for batch operations.



```
from odoo import models, api

class MyModel(models.Model):
    _name = 'my.model'

 @api.multi
    def perform_batch_operation(self):
        for record in self:
            # Your batch operation logic here
```

6.  **@api.one**: Deprecated in Odoo 10 and removed in Odoo 11. Used for methods that operate on a single record.

These are some of the commonly used `@api` decorators in Odoo. Keep in mind that the decorators available may vary depending on the Odoo version you're using. Always refer to the official Odoo documentation for the version-specific information and usage details.

## ORM methods
In Odoo, ORM (Object-Relational Mapping) methods are used to interact with the database records of models. ORM methods provide a high-level and Pythonic way to perform database operations like creating, reading, updating, and deleting records. Here are some commonly used ORM methods with examples:

1.  **Creating Records**:
    -   `create()`: Used to create new records in the database.


```
from odoo import models, fields

class MyModel(models.Model):
    _name = 'my.model'

    name = fields.Char(string='Name')
```
### Creating a new record
new_record = self.env['my.model'].create({'name': 'New Record Name'})` 

2.  **Reading Records**:
    -   `search()`: Used to search for records based on certain conditions.
    -   `browse()`: Used to retrieve specific records by their IDs.

pythonCopy code

```# Searching for records
records = self.env['my.model'].search([('name', '=', 'Target Name')])
```
### Browsing records by ID
```record = self.env['my.model'].browse(record_id)```

3.  **Updating Records**:
    -   `write()`: Used to update existing records.

```

`# Updating a record
record_to_update.write({'name': 'Updated Name'}) 
```
4.  **Deleting Records**:
    -   `unlink()`: Used to delete records from the database.



```# Deleting a record
record_to_delete.unlink()
```
5.  **Computed Fields**:
    -   Computed fields are fields that are automatically calculated based on other fields' values. They are defined using the `@api.depends` decorator and computed methods.



```from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.model'

    field_a = fields.Float(string='Field A')
    field_b = fields.Float(string='Field B')
    computed_field = fields.Float(string='Computed Field', compute='_compute_field')

 @api.depends('field_a', 'field_b')
    def _compute_field(self):
        for record in self:
            record.computed_field = record.field_a + record.field_b
```
6.  **Constraints**:
    -   Constraints ensure that certain conditions are met before allowing records to be saved in the database. They are defined using the `@api.constrains` decorator and constraint methods.



```from odoo import models, fields, api

class MyModel(models.Model):
    _name = 'my.model'

    field_c = fields.Float(string='Field C')

 @api.constrains('field_c')
    def _check_field_c(self):
        for record in self:
            if record.field_c < 0:
                raise models.ValidationError("Field C cannot be negative.") 
```
These are some examples of how ORM methods are used in Odoo.