from odoo import models, fields, api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("stock.dock", string="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one(related="vehicle_id.category_id", string="Vehicle Category", readonly=False)
    weight = fields.Float(compute="_compute_weight")
    volume = fields.Float(compute="_compute_volume")
    progress_volume = fields.Float()
    progress_weight = fields.Float()

    @api.depends("move_line_ids.product_id.weight","vehicle_category_id.max_weight")
    def _compute_weight(self):
        for record in self:
            record.weight = sum(line.product_id.weight*line.quantity for line in record.move_line_ids)

        if record.weight and record.vehicle_category_id.max_weight:
            record.progress_weight = record.weight/record.vehicle_category_id.max_weight*100
        else:
            record.progress_weight = 0

    @api.depends("move_line_ids.product_id.volume","vehicle_category_id.max_volume")
    def _compute_volume(self):
        for record in self:
            record.volume = sum(line.product_id.volume*line.quantity for line in record.move_line_ids)

        if record.volume and record.vehicle_category_id.max_volume:
            record.progress_volume = record.volume/record.vehicle_category_id.max_volume*100
        else:
            record.progress_volume = 0
    
    
