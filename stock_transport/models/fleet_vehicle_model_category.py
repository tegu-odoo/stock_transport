from odoo import models, fields, api

class FleetVehicleModelCategory(models.Model):
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Integer(string="Max Weight(Kg)")
    max_volume = fields.Integer(string="Max Volume(m3)")

    @api.depends("max_weight", "max_volume")
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name + '(' + str(record.max_weight) + 'Kg, ' + str(record.max_volume) + 'm3 )'
        return True
      
    