import time
from lxml import etree
import openerp.addons.decimal_precision as dp
import openerp.exceptions

from openerp import netsvc
from openerp import pooler
from openerp.osv import fields, osv, orm
from openerp.tools.translate import _

class account_invoice(osv.osv):
    _name = 'account.invoice'    
    _inherit = 'account.invoice'    
    _description = 'Invoice'

    def refund(self, cr, uid, ids, date=None, period_id=None, description=None, journal_id=None, context=None):
        new_ids = []
        mrp_repair_obj = self.pool.get('mrp.repair')
        for invoice in self.browse(cr, uid, ids, context=context):        	
        	repair_obj = mrp_repair_obj.search(cr, uid, [('name','=', invoice.origin)])
        	mrp_repair_obj.write(cr, uid, [l for l in repair_obj], {'state': 'avoir'})
        	invoice = self._prepare_refund(cr, uid, invoice, date=date, period_id=period_id, description=description, journal_id=journal_id,context=context)
        	new_ids.append(self.create(cr, uid, invoice, context=context))
        	
        return new_ids
account_invoice()
