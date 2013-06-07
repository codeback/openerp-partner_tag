from osv import osv, fields

class sale_order(osv.osv):
    _name = 'sale.order'
    _inherit = 'sale.order'

    _columns = {     
       'partner_category_id': fields.related('partner_id', 'category_id', type='many2many', relation="res.partner.category", string='Tags', readonly=True),
    }