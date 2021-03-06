
from osv import fields, osv

class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Partner'

    _defaults = {
#        'property_account_receivable' : 290, #Fournisseur , Table account_account_template  
#        'property_account_payable' : 365,
        'ref': lambda obj, cr, uid, context:  obj.pool.get('ir.sequence').get(cr, uid, 'res.fournisseur') if context.get('default_customer') == False else  obj.pool.get('ir.sequence').get(cr, uid, 'res.client'),     
    }
    
    _sql_constraints = [
        ('uniq_ref', 'unique(ref)', "The Reference must be unique"),
    ]
    
res_partner()
