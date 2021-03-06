from osv import osv, fields

class account_invoice(osv.osv):
    _name = 'account.invoice.report'
    _inherit = 'account.invoice.report'

    _columns = {     
       'partner_category_id': fields.related('partner_id', 'category_id', type='many2many', relation="res.partner.category", string='Tags', readonly=True),
    }