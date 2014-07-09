import decimal_precision as dp
from osv import osv, fields
from tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from tools.translate import _

class purchase_order(osv.osv):
    _name = "purchase.order"
    _inherit = 'purchase.order'  

                 
    _columns = {
 #       'transport' : fields.float('Transport'),
 #       'douane' : fields.float('Douane'),
 #       'transit' : fields.float('Transit'),
 #       'divers' : fields.float('Divers'),
 #       'totale_facture' : fields.float('Total facture')    
    }    
        
purchase_order()
