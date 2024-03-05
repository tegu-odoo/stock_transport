from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    volume_transfer = fields.Float(compute="_compute_volume_transfer", string="Volume")
    weight_transfer = fields.Float(compute="_compute_weight_transfer", string="Weight")
    
    @api.depends("move_ids.product_id.volume")
    def _compute_volume_transfer(self):
        for record in self:
            record.volume_transfer = sum(line.product_id.volume*line.quantity for line in record.move_ids)
        return True
