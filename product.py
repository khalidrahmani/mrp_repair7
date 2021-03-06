
from osv import fields, osv

class code_marque(osv.osv):
    
    _name = 'code.marque'
    _description = "Code Marque"
    _order = "name"
    _columns = {
        'name': fields.char("Code Marque", size=64),
    }
    
    _sql_constraints = [
        ('uniq_name', 'unique(name)', "The Name must be unique"),
    ]
    
code_marque()

class similar_product_line(osv.osv):
    _name = 'similar.product.line'        
    _description = 'similar product line'    
    
    _columns = {
        'product_id_ref': fields.many2one('product.product', 'Product Ref',ondelete='cascade', select=True),                
        'product_id': fields.many2one('product.product', 'Product', domain=[('sale_ok','=',True)], required=True),                
    }
                        
similar_product_line()    

class product_product(osv.osv):

    _name = 'product.product'    
    _inherit = 'product.product'    
    _description = 'Product'
            
    _columns = {
        'code_marque': fields.many2one('code.marque','Code Marque'),        
        'similar_products' : fields.one2many('similar.product.line', 'product_id_ref', 'Similar Products'),  
        'casier' : fields.char('Casier', size=64),
        'casier2' : fields.char('Casier2', size=64),          
        'default_code' : fields.char('Internal Reference', size=64, select=True, required=True),  
    }    
    
    _defaults = {
        'property_account_income' : 726, 
        'property_account_expense' : 469, 
        'type' : 'product'   
    }

    _sql_constraints = [
        ('uniq_reference', 'unique(default_code)', "La reference doit etre unique"),
    ]
product_product()